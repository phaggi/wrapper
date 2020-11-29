import subprocess
import sys
import re
from pathlib import Path
from pprint import pprint

from wrap_tools import get_wrapped_tool_path


def get_arguments(_args, _arguments):
    new_argument_key = ''
    for _element in _args:
        if _element in _arguments.keys():
            new_argument_key = _element
            if not _arguments[_element]:
                _arguments[_element] = True
        elif new_argument_key != '':
            if ',' in _element:
                _elements = _element.split(',')
            else:
                _elements = [_element]
            for _subelement in _elements:
                if type(_arguments[new_argument_key]) == type(list()):
                    _arguments[new_argument_key].append(_subelement)
                elif type(_arguments[new_argument_key]) != type(list()) and type(_arguments[new_argument_key]) != type(
                        bool()):
                    _arguments[new_argument_key] = [_arguments[new_argument_key], _subelement]
                else:
                    _arguments[new_argument_key] = _subelement
        else:
            print('argument {} havn\'t key'.format(_element))
    return _arguments


def split_args(all_args, wrapped_args_patterns, wrapper_args_patterns):
    """
    Args:
        all_args(list):
            All arguments.

        wrapped_args_patterns(list):
            Regular expressions with patterns of wrapper arguments.

    Returns:
        tuple([args_for_wrapped], [args_for_wrapper])
    """
    all_args = get_arguments(all_args)
    _base_args = {}
    _wrapper_args = {}
    # Find all of wrapper args in all_args
    for key, value in all_args.items():
        if key in wrapped_args_patterns:
            _base_args.update({key: value})
        elif key in wrapper_args_patterns:
            _wrapper_args.update({key: value})
        else:
            pass
            # print('not found {}: {}'.format(key, value))

    """for w_arg_pattern in wrapped_args_patterns:
        found_args = re.findall(w_arg_pattern, all_args)
        for found_arg in found_args:
            # Add them to new list
            w_args.extend(found_arg)
            # Remove them from all_args
            all_args = all_args.replace(' '.join(found_arg), '')
    all_args = all_args.split()"""
    pprint(_base_args)
    return _base_args, _wrapper_args


# wrapper arguments
"""w_args_patterns = [
    r'(-f) (json|toml)',
]
"""

base_args, w_args = split_args(sys.argv[1:], wr)

# using a wrapper args in wrapper
...

# run wrapped.py with other args
# base_args = sys.argv
print('wrapper  : {}'.format(w_args))
print('mywrapp  : {}'.format(base_args))
base_args_string = ''
for key, value in base_args.items():
    base_args_string += ' ' + key
    for element in value:
        base_args_string += ' ' + element
    base_args_string = base_args_string.strip()
subprocess.call(' '.join(['python', get_wrapped_tool_path(), base_args_string]),
                shell=True)
