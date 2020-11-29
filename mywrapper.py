import subprocess
import sys
import re
from pathlib import Path
from pprint import pprint

from wrappersplitters import split_by_key
from wrap_tools import get_wrapped_tool_path

import re

def parse_keys(_arg, _separators=None):
    if not _separators:
        _separators = '=|:| |,'
    _arg = re.split(_separators, _arg)
    _key = _arg[0]
    _value = True
    if len(_arg) == 2:
        _value = _arg[1]
    if len(_arg) > 2:
        _value = _arg[1:]
    return _key, _value


def make_arg_dict(_args):
    _new_arg_dict = {}
    for _arg in _args:
        _key, _value = parse_keys(_arg)
        if _key not in _new_arg_dict.keys():
            _new_arg_dict.update({_key: _value})
        else:
            if isinstance(_new_arg_dict[_key], str):
                _new_arg_dict[_key] = [_new_arg_dict[_key]]
            if isinstance(_value, str):
                _value = [_value]
            _new_arg_dict[_key].extend(_value)
    return _new_arg_dict


def split_args(_all_args: str, wrapped_args_patterns: list, wrapper_args_patterns: list):
    """
    Args:
        :param _all_args: str
            All arguments in str.

        :param wrapped_args_patterns: list of wrapped app arguments.
        :param wrapper_args_patterns: list of wrapper script arguments.
    Returns:
        tuple([args_for_wrapped], [args_for_wrapper])

    """
    _base_args = {}
    _wrapper_args = {}
    _all_args = make_arg_dict(split_by_key(_all_args))
    pprint(_all_args)
    # Find all of wrapper args in all_args
    for _key, _value in _all_args.items():
        print('mywrapper.split_args {} {}'.format(_key, _value))
        if _key in wrapped_args_patterns:
            _base_args.update({_key: _value})
        elif _key in wrapper_args_patterns:
            _wrapper_args.update({_key: _value})
        else:
            pass
    return _base_args, _wrapper_args


# wrapper arguments
"""w_args_patterns = [
    r'(-f) (json|toml)',
]
"""
all_args = ' '.join(sys.argv[1:])
print('mywrapper:all_args {} {}'.format(type(all_args), all_args))
base_keys = ['-verbose', '-format', '-i', '-sort', '-linters', '-skip', '-report', '-async',
             '-options', '-force']
wrapper_keys = ['']
base_args, w_args = split_args(all_args, base_keys, wrapper_keys)

# using a wrapper args in wrapper
...

# run wrapped.py with other args
# base_args = sys.argv
print('wrapper  : {}'.format(w_args))
print('mywrapp  : {}'.format(base_args))


def run_subprocess(_base_args):
    base_args_string = ''
    for key, value in _base_args.items():
        base_args_string += ' ' + key
        if isinstance(value, bool):
            pass
        elif isinstance(value, list):
            for element in value:
                base_args_string += ' ' + element
        elif isinstance(value, str):
            base_args_string += ' ' + value
        base_args_string = base_args_string.strip()
    subprocess.call(' '.join(['python', get_wrapped_tool_path(), base_args_string]),
                    shell=True)


run_subprocess(base_args)

'''example = '--verbose --format parsable -i W501 W100 --sort W,D,W -f json ' \
          '--linters mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,pylint ' \
          '--skip messages.py --skip ./config.settings apps.first_app ' \
          '--msg-template=../wrapper_msg_template.json --report ../report.txt ' \
          '--async --options setup.cfg -r no --force .'
          '''
# args = split_by_key(example)
