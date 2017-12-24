#include "spell_corrector.hpp"

namespace NOpenSpell {


bool TSpellCorrector::LoadLangModel(const std::string& modelFile) {
    return LangModel.Load(modelFile);
}

struct TScoredWord {
    TWord Word;
    double Score = 0;
};

TWords TSpellCorrector::Correct(const TWords& sentence, size_t position) {
    if (position >= sentence.size()) {
        return TWords();
    }

    TWord w = sentence[position];
    TWords candidates = Edits(w);
    bool firstLevel = true;
    if (candidates.empty()) {
        candidates = Edits(w, false);
        firstLevel = false;
    }

    {
        TWord c = LangModel.GetWord(std::wstring(w.Ptr, w.Len));
        if (c.Ptr && c.Len) {
            w = c;
            candidates.push_back(c);
        }
    }

    if (candidates.empty()) {
        return candidates;
    }

    std::unordered_set<TWord, TWordHashPtr> uniqueCandidates(candidates.begin(), candidates.end());
    std::vector<TScoredWord> scoredCandidates;
    scoredCandidates.reserve(candidates.size());
    for (TWord cand: uniqueCandidates) {
        TWords candSentence;
        for (size_t i = 0; i < sentence.size(); ++i) {
            if (i == position) {
                candSentence.push_back(cand);
            } else {
                candSentence.push_back(sentence[i]);
            }
        }

        TScoredWord scored;
        scored.Word = cand;
        scored.Score = LangModel.Score(candSentence);
        if (!(scored.Word == w)) {
            if (firstLevel) {
                scored.Score *= 1.045;
            } else {
                scored.Score *= 50.0;
            }
        }
        scoredCandidates.push_back(scored);
    }

    std::sort(scoredCandidates.begin(), scoredCandidates.end(), [](TScoredWord w1, TScoredWord w2) {
        return w1.Score > w2.Score;
    });

    candidates.clear();
    for (auto s: scoredCandidates) {
        candidates.push_back(s.Word);
    }
    return candidates;
}

template<typename T>
inline void AddVec(T& target, const T& source) {
    target.insert(target.end(), source.begin(), source.end());
}

TWords TSpellCorrector::Edits(const TWord& word, bool lastLevel) {
    std::wstring w(word.Ptr, word.Len);
    TWords result;

    for (size_t i = 0; i < w.size() - 1; ++i) {

        // delete
        {
            std::wstring s = w.substr(0, i) + w.substr(i+1);
            TWord c = LangModel.GetWord(s);
            if (c.Ptr && c.Len) {
                result.push_back(c);
            }
            if (!lastLevel) {
                AddVec(result, Edits(TWord(s)));
            }
        }

        // transpose
        if (i < w.size() - 2) {
            std::wstring s = w.substr(0, i);
            s += w.substr(i + 1, 1);
            s += w.substr(i, 1);
            if (i < w.size() - 3) {
                s += w.substr(i+2);
            }
            TWord c = LangModel.GetWord(s);
            if (c.Ptr && c.Len) {
                result.push_back(c);
            }
            if (!lastLevel) {
                AddVec(result, Edits(TWord(s)));
            }
        }

        // replace
        {
            for (auto&& ch: LangModel.GetAlphabet()) {
                std::wstring s = w.substr(0, i) + ch + w.substr(i+1);
                TWord c = LangModel.GetWord(s);
                if (c.Ptr && c.Len) {
                    result.push_back(c);
                }
                if (!lastLevel) {
                    AddVec(result, Edits(TWord(s)));
                }
            }
        }

        // inserts
        {
            for (auto&& ch: LangModel.GetAlphabet()) {
                std::wstring s = w.substr(0, i) + ch + w.substr(i);
                TWord c = LangModel.GetWord(s);
                if (c.Ptr && c.Len) {
                    result.push_back(c);
                }
                if (!lastLevel) {
                    AddVec(result, Edits(TWord(s)));
                }
            }
        }
    }

    return result;
}


} // NOpenSpell