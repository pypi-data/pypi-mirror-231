from .a_imports import *

"""
This file contains all the constants used in the project.
"""

TE = TypeVar("TE")
"""this represents a generic type of something we'll read from the env"""


def get_env(
    var_name: str,
    default_value: TE,
) -> TE:
    """get an environment variable and type cast it, or return a default value if it's not set"""
    value = os.environ.get(var_name)

    if value is None:
        return default_value

    try:
        return type(default_value)(value)
    except ValueError:
        print(f"Could not cast {var_name}={value} to {type(default_value)}")
        return default_value

