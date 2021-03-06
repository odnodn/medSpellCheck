# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_jamspell')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_jamspell')
    _jamspell = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_jamspell', [dirname(__file__)])
        except ImportError:
            import _jamspell
            return _jamspell
        try:
            _mod = imp.load_module('_jamspell', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _jamspell = swig_import_helper()
    del swig_import_helper
else:
    import _jamspell
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _jamspell.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _jamspell.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _jamspell.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _jamspell.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _jamspell.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _jamspell.SwigPyIterator_equal(self, x)

    def copy(self):
        return _jamspell.SwigPyIterator_copy(self)

    def next(self):
        return _jamspell.SwigPyIterator_next(self)

    def __next__(self):
        return _jamspell.SwigPyIterator___next__(self)

    def previous(self):
        return _jamspell.SwigPyIterator_previous(self)

    def advance(self, n):
        return _jamspell.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _jamspell.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _jamspell.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _jamspell.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _jamspell.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _jamspell.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _jamspell.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _jamspell.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import collections
class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _jamspell.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _jamspell.StringVector___nonzero__(self)

    def __bool__(self):
        return _jamspell.StringVector___bool__(self)

    def __len__(self):
        return _jamspell.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _jamspell.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _jamspell.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _jamspell.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _jamspell.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _jamspell.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _jamspell.StringVector___setitem__(self, *args)

    def pop(self):
        return _jamspell.StringVector_pop(self)

    def append(self, x):
        return _jamspell.StringVector_append(self, x)

    def empty(self):
        return _jamspell.StringVector_empty(self)

    def size(self):
        return _jamspell.StringVector_size(self)

    def swap(self, v):
        return _jamspell.StringVector_swap(self, v)

    def begin(self):
        return _jamspell.StringVector_begin(self)

    def end(self):
        return _jamspell.StringVector_end(self)

    def rbegin(self):
        return _jamspell.StringVector_rbegin(self)

    def rend(self):
        return _jamspell.StringVector_rend(self)

    def clear(self):
        return _jamspell.StringVector_clear(self)

    def get_allocator(self):
        return _jamspell.StringVector_get_allocator(self)

    def pop_back(self):
        return _jamspell.StringVector_pop_back(self)

    def erase(self, *args):
        return _jamspell.StringVector_erase(self, *args)

    def __init__(self, *args):
        this = _jamspell.new_StringVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _jamspell.StringVector_push_back(self, x)

    def front(self):
        return _jamspell.StringVector_front(self)

    def back(self):
        return _jamspell.StringVector_back(self)

    def assign(self, n, x):
        return _jamspell.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _jamspell.StringVector_resize(self, *args)

    def insert(self, *args):
        return _jamspell.StringVector_insert(self, *args)

    def reserve(self, n):
        return _jamspell.StringVector_reserve(self, n)

    def capacity(self):
        return _jamspell.StringVector_capacity(self)
    __swig_destroy__ = _jamspell.delete_StringVector
    __del__ = lambda self: None
StringVector_swigregister = _jamspell.StringVector_swigregister
StringVector_swigregister(StringVector)

class TSpellCorrector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TSpellCorrector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TSpellCorrector, name)
    __repr__ = _swig_repr

    def LoadLangModel(self, modelFile):
        return _jamspell.TSpellCorrector_LoadLangModel(self, modelFile)

    def TrainLangModel(self, textFile, alphabetFile, modelFile):
        return _jamspell.TSpellCorrector_TrainLangModel(self, textFile, alphabetFile, modelFile)

    def GetCandidatesScoredRaw(self, sentence, position):
        return _jamspell.TSpellCorrector_GetCandidatesScoredRaw(self, sentence, position)

    def GetCandidatesRaw(self, sentence, position):
        return _jamspell.TSpellCorrector_GetCandidatesRaw(self, sentence, position)

    def GetALLCandidatesScoredJSON(self, text):
        return _jamspell.TSpellCorrector_GetALLCandidatesScoredJSON(self, text)

    def GetCandidatesScored(self, sentence, position):
        return _jamspell.TSpellCorrector_GetCandidatesScored(self, sentence, position)

    def GetCandidates(self, sentence, position):
        return _jamspell.TSpellCorrector_GetCandidates(self, sentence, position)

    def FixFragment(self, text):
        return _jamspell.TSpellCorrector_FixFragment(self, text)

    def FixFragmentNormalized(self, text):
        return _jamspell.TSpellCorrector_FixFragmentNormalized(self, text)

    def SetPenalty(self, knownWordsPenaly, unknownWordsPenalty):
        return _jamspell.TSpellCorrector_SetPenalty(self, knownWordsPenaly, unknownWordsPenalty)

    def SetMaxCandidatesToCheck(self, maxCandidatesToCheck):
        return _jamspell.TSpellCorrector_SetMaxCandidatesToCheck(self, maxCandidatesToCheck)

    def GetLangModel(self):
        return _jamspell.TSpellCorrector_GetLangModel(self)

    def __init__(self):
        this = _jamspell.new_TSpellCorrector()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _jamspell.delete_TSpellCorrector
    __del__ = lambda self: None
TSpellCorrector_swigregister = _jamspell.TSpellCorrector_swigregister
TSpellCorrector_swigregister(TSpellCorrector)

# This file is compatible with both classic and new-style classes.


