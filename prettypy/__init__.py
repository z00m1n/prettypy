import codecs

from .printer import Printer

__version__ = '0.5.0'

def dump(what, **kw):
    ''' Dump a data structure to stdout and to a file.

    The output to stdout uses the default parameters.
    The parameters for output to the file may be specified as key-args.
    The name and the ext of the output file may be specified as well.
    The name defaults to "prettypy" and the ext to "dump".
    '''
    if kw.pop('default', True):
        Printer().print(what)
    arg = dict(
        sort      = False,
        types     = False,
        max_seq   = 99,
        max_map   = 99,
        max_str   = 99,
        max_lines = 33,
        max_depth =  9,
    )
    name = kw.pop('name', 'prettypy')
    name, ext = name.split('.') if '.' in name else (name, 'dump')
    arg.update(kw)
    with codecs.open('%s.%s' % (name, ext), 'w', encoding='utf-8') as out:
        Printer(target=out, **arg).print(what)
