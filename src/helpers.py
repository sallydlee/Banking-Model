import random
import string
import datetime


def check_date(date_str):
    """
    Checks if input is a valid date.

    Parameters
    ----------
    date_str : str
        String to convert to date

    Returns
    -------
    Date
    """

    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date.")


def check_int(user_input):
    """
    Checks if input is an integer.

    Parameters
    ----------
    user_input : int

    Returns
    -------
    Integer
    """

    try:
        return int(user_input)
    except ValueError:
        print("Please use an integer value.")


def read_int(prompt_msg, error_msg):
    """
    Checks if user input is an integer.
    Parameters
    ----------
    prompt_msg : str
        Prompt message user responds to.
    error_msg : str
        Desired error message if ValueError is thrown.

    Returns
    -------
    Integer
    """
    while True:
        try:
            return int(input(prompt_msg))
        except ValueError:
            print(error_msg)


def random_number(length):
    """
    Returns random string of digits of given length.

    Parameters
    ----------
    length : int
        Length of generated string.

    Returns
    -------
    String
    """
    return ''.join(random.choices(string.digits, k=length))







