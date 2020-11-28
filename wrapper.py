import sys
import re

import get_wrapped_tool_path()


def split_args(all_args, w_args_patterns):
    """
    Args:
        all_args(list):
            All arguments.

        w_args_patterns(list):
            Regular expressions with patterns of wrapper arguments.

    Returns:
        tuple([args_for_wrapped], [args_for_wrapper])
    """
    all_args = ' '.join(all_args)
    w_args = []
    # Find all of wrapper args in all_args
    for w_arg_pattern in w_args_patterns:
        found_args = re.findall(w_arg_pattern, all_args)
        for found_arg in found_args:
            # Add them to new list
            w_args.extend(found_arg)
            # Remove them from all_args
            all_args = all_args.replace(' '.join(found_arg), '')
    all_args = all_args.split()
    return all_args, w_args


# wrapper arguments
w_args_patterns = [
    r'(-f) (json|toml)',
]

base_args, w_args = split_args(
    sys.argv[1:],
    w_args_patterns
)

# using a wrapper args in wrapper
...

# run wrapped with other args
subprocess.run(
    ' '.join([get_wrapped_tool_path()] + base_args)
)