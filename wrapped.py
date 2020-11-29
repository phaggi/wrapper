import sys
target_args = ['--verbose', '--format', 'parsable', '-i', 'W501', 'W100', '--sort', 'W,D,W', '--linters', 'mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,pylint', '--skip', 'messages.py', '--skip', './config.settings', 'apps.first_app', '--report', '../report.txt', '--async', '--options', 'setup.cfg', '--force', '.']
in_args = sys.argv[1:]
print(in_args)
for element in target_args:
    try:
        in_args.remove(element)
    except:
        print('не найден {}'.format(element))
print(in_args)