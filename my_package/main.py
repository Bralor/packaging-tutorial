"""Main function"""
from my_package.common.utils import get_todays_date


def my_func():
    print(
        f"""
    Running the main file,
    TODAY: {get_todays_date()}
    End of function
    """
    )
