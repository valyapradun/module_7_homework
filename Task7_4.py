"""
Implement decorator for suppressing exceptions. If exception not occurred write log to console.
"""
import functools


def exceptions_suppressing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print('Exception was not occurred! Result: ' + str(result))
            return result
        except Exception as exc:
            print('The following exception was suppressed: ' + exc.__str__())
            return None
    return wrapper


@exceptions_suppressing_decorator
def test_zero_divide(x, y):
    return x / y


@exceptions_suppressing_decorator
def test_string_multiplication (x, y):
    return x * y


if __name__ == '__main__':
    test_zero_divide(2, 0)
    test_zero_divide(2, 2)
    test_string_multiplication(2, 2)
    test_string_multiplication('2', '2')



