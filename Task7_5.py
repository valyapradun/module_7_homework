"""
Implement a function to check that number is even (number > 3).
A number should be passed as a string.
Throw different exceptions for different situations.
Custom exceptions must be derived from custom base exception (not Base Exception class).
"""


class CustomException(Exception):
    pass


class LessException(CustomException):
    pass


class EvenException(CustomException):
    pass


def even_number(number: str) -> bool:
    try:
        int_number = int(number)
    except Exception as err:
        raise CustomException(f'Number {number} should be integer') from err

    if int_number < 3:
        raise LessException(f'Number {number} must be greater than 3')

    if int_number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(even_number('7'))
    print(even_number('224'))
    print(even_number('0'))
    print(even_number('qwerty'))

