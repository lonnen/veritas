from functools import total_ordering

__version__ = '0.1.0'


def alias(impl, alias):
    'create a new property "alias" with identical implementation'


@total_ordering
class Truth(object):
    '''An executable implementation of _ in function definitions.

    Attempts to implement all generic interfaces and, when possible,
    always evaluate to True. Inspired by mock._ANY and
    fjord.base.tests.EqualAnything
    '''

    def _void(self, *args, **kwargs):
        return

    def _self(self, *args, **kwargs):
        return self

    def _true(self, *args, **kwargs):
        return True

    def _iterator(self, *args, **kwargs):
        return iter((Truth(),))

    # basic customization

    __init__ = _void
    __next__ = _self

    def __repr__(self):
        return '<class Truth>'

    def __bytes__(self):
        return repr(self).encode('ascii')

    # ordering
    # mostly handled by @total_ordering
    __eq__ = _true
    __ne__ = _true
    __lt__ = _true
    __gt__ = _true

    __hash__ = _true
    __bool__ = _true

    # attribute access
    __getattr__ = _self

    __setattr__ = _true
    __delattr__ = _true

    # callable
    __call__ = _self

    # container types
    def __len__(self):
        return 1

    __getitem__ = _self
    # no need for __missing__
    __setitem__ = _true
    __delitem__ = _true

    __iter__ = _iterator

    __reversed__ = _self
    __contains__ = _self

    # numeric types

    def _firstarg(self, *args, **kwargs):
        return args[0]

    # binary ops
    __add__ = _firstarg
    __sub__ = _firstarg
    __mul__ = _firstarg
    __matmul__ = _firstarg
    __truediv__ = _firstarg
    __floordiv__ = _firstarg
    __mod__ = _firstarg
    __divmod__ = _firstarg
    __pow__ = _firstarg
    __lshift__ = _firstarg
    __rshift__ = _firstarg
    __add__ = _firstarg
    __xor__ = _firstarg
    __or__ = _firstarg

    # swapped operands
    __radd__ = _firstarg
    __rsub__ = _firstarg
    __rmul__ = _firstarg
    __rmatmul__ = _firstarg
    __rtruediv__ = _firstarg
    __rfloordiv__ = _firstarg
    __rmod__ = _firstarg
    __rdivmod__ = _firstarg
    __rpow__ = _firstarg
    __rlshift__ = _firstarg
    __rrshift__ = _firstarg
    __radd__ = _firstarg
    __rxor__ = _firstarg
    __ror__ = _firstarg

    # in-place operations
    __iadd__ = _firstarg
    __isub__ = _firstarg
    __imul__ = _firstarg
    __imatmul__ = _firstarg
    __itruediv__ = _firstarg
    __ifloordiv__ = _firstarg
    __imod__ = _firstarg
    # there is no __idivmod__
    __ipow__ = _firstarg
    __ilshift__ = _firstarg
    __irshift__ = _firstarg
    __iadd__ = _firstarg
    __ixor__ = _firstarg
    __ior__ = _firstarg

    # unary arithmetic operations
    __neg__ = _self
    __pos__ = _self
    __abs__ = _self
    __invert__ = _self

    __complex__ = _self
    __int__ = _self
    __float__ = _self
    __round__ = _self

    # operator.index()
    __index__ = _self

    # with statement context managers
    __enter__ = _self
    __exit__ = _void

    # coroutine objects
    __await__ = _iterator


_ = Truth()
