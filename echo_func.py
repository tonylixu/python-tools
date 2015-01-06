from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
'''A module helps you trace function call's arguments.

    To use it, just use "@echo" to decorate fucntions
you want to trace its arguments.

    Example:
        @echo
        def h(x=1, y=2): pass
        will output:
        =============
        positional arguments: []
        defaulted arguments: [u'x=1', u'y=2']
        nameless arguments:[]
        keyword arguments:[]
        h(x=1, y=2)

   idea borrowed from:
      http://wordaligned.org/articles/echo

'''
import sys

def main():
    @echo
    def f(x): pass

    @echo
    def g(x, y): pass

    @echo
    def h(c, d, x=1, y=2): pass

    @echo
    def i(x, y, *v): pass

    @echo
    def j(x, y, *v, **k): pass

    class X(object):
        @echo
        def m(self, x): pass
        @classmethod
        @echo
        def cm(klass, x): pass

    f(10)
    g('spam', 42)
    g(y="spam", x=42)
    h('test', 'test2')
    i("spam", 42, "extra", "args", 1, 2, 3)
    j(("green", "eggs"), y="spam", z=42)
    X().m("method call")
    X.cm("classmethod call")

def format_arg_value(arg_val):
    '''Return a string representing a (name, value) pair.

    >>> format_arg_value(('x', (1, 2, 3)))
    'x=(1, 2, 3)'
    '''
    arg, val = arg_val
    return '{}={}'.format(arg, val)

def echo(fn, write=sys.stdout.write):
    '''Echo calls to a function.

    Returns a decorated version of the input function which "echoes" calls
    made to it by writing out the function's name and the arguments it was
    called with.
    '''

    import functools
    # Unpack function's arg count, arg names, arg defaults
    code = fn.func_code
    argcount = code.co_argcount  # Number of arguments
    argnames = code.co_varnames[:argcount]  # Arguments name
    fn_defaults = fn.func_defaults or list() # Default value or empty list
    # Since you can't have a non-keyword argument after keyword argument, i.e
    # foo(a=1, b=2, c, d) is illegal, foo(c, d, a=1, b=2) is okay, so default
    # arguments always after positional
    # use [-:] to combine arguments and definitions into dict
    argdefs = dict(zip(argnames[-len(fn_defaults):], fn_defaults))

    @functools.wraps(fn)
    def wrapped(*v, **k):  # Any number of arguments
        # Collect function argumetns by chaining together positional,
        # defaulted, extra positional and keyword arguments.
        positional = map(format_arg_value, zip(argnames, v))
        defaulted = [format_arg_value((a, argdefs[a]))
                        for a in argnames[len(v):] if a not in k]
        nameless = map(repr, v[argcount:])
        keyword = map(format_arg_value, k.items())
        args = positional + defaulted + nameless + keyword
        write('{}({})\n\n'.format(fn.func_name, ", ".join(args)))
        return fn(*v, **k)
    return wrapped

if __name__ == '__main__':
    main()
