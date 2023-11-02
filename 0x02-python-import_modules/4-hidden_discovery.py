#!/usr/bin/python3

import dis
import hidden_4


def print_names_from_pyc(pyc_file):

    with open(pyc_file, 'rb') as file:
        code = file.read()
        code_object = compile(code, '', 'exec')
        names = [c.co_name
                 for c in code_object.co_consts
                 if isinstance(c, type(code_obj))]
        sorted_names = sorted(name
                              for name in names
                              if not name.startswith('__'))
        for name in sorted_names:
            print(name)


if __name__ == '__main__':
    pyc_file = 'hidden_4'
    print_names_from_pyc(pyc_file)
