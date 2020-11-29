import subprocess

from wrap_tools import get_wrapped_tool_path
my_wrapper = '/Users/phaggi/PycharmProjects/wrapper/mywrapper.py'
base_args = "--verbose --format parsable -i W501 W100 --sort W,D,W -f json " \
            "--linters mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,pylint " \
            "--skip messages.py --skip ./config.settings apps.first_app --msg-template=../wrapper_msg_template.json " \
            "--report ../report.txt --async --options setup.cfg -r no --force ."
my_command = ' '.join(['python', my_wrapper, base_args])
#  print('command: {}'.format(my_command))
subprocess.call(my_command, shell=True)
