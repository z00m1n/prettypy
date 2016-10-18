'''
    Convenience functions for prettypy tests.
'''

import codecs
from sys import exit
from io import StringIO
from itertools import zip_longest

from prettypy import __version__, Printer, dump

print('prettypy version %s' % __version__)

def check_result(result, expected_output):
    for lin, (exp, res) in enumerate(zip_longest(expected_output.split('\n'), result.split('\n'))):
        if exp!=res:
            print('\n\tline %s :\nexp : %s\ngot : %s\n'%(lin, exp, res))
            break
    if result!=expected_output:
        print('\tresult :\n', '\n'.join('%3i %s'%(i,s) for i,s in enumerate(result.split('\n'))))
        print(next('\n\tpos %i :\n%s'%(i,t) for i,t in enumerate(zip_longest(expected_output, result)) if t[0]!=t[1]))
        return False
    return True

def check_printer(input_object, expected_output, **kw):
    kw.pop('name', '')
    out = StringIO()
    p = Printer(target=out, **kw)
    p.print(input_object)
    return check_result(out.getvalue(), expected_output)

def check_dump(input_object, expected_output, **kw):
    name = kw.get('name', 'prettypy.dump')
    name = '/tmp/'+name
    kw['name'] = name
    dump(input_object, default=False, **kw)
    with codecs.open(name, 'r', encoding='utf-8') as out:
        return check_result(out.read(), expected_output)

def check(input_object, expected_output, **kw):
    if (check_printer(input_object, expected_output, **kw)
        and check_dump(input_object, expected_output, **kw)
    ):
        print('.', end='')
    else:
        print('\n\tKO !')
        exit(1)
