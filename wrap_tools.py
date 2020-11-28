from pathlib import Path

my_file_path = '/Users/phaggi/PycharmProjects/wrapper/wrapped'
def get_wrapped_tool_path():
    return str(Path(my_file_path))


if __name__ == '__main__':
    print(get_wrapped_tool_path())
