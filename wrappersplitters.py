from pprint import pprint


def split_by_key(_args: str):
    """
    :param _args: string of arguments
    :return: list of arguments with values
    """
    _args = _args.split('--')
    _new_args = []
    for element in _args:
        if '-' in element:
            element = element.split('-')
            element[0] = ''.join(['--', element[0]])
            _subelements = element[1:]
            for number, _subelement in enumerate(_subelements):
                element[number + 1] = '-' + _subelement
        else:
            element = ''.join(['--', element])
        if isinstance(element, str):
            _new_args.append(element.strip())
        elif isinstance(element, list):
            for _anothersubelement in element:
                _new_args.append(_anothersubelement.strip())
    _new_args.remove('--')
    return _new_args


if __name__ == '__main__':
    base_args = "--verbose --format parsable -i W501 W100 --sort W,D,W -f json " \
                "--linters mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,pylint " \
                "--skip messages.py --skip ./config.settings apps.first_app --msg-template=../wrapper_msg_template.json " \
                "--report ../report.txt --async --options setup.cfg -r no --force ."

    pprint(split_by_key(base_args))
