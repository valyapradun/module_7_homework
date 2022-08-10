"""
Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing 'q' program succesfully close.
Use function from Task 7.5 for validating input, handle all exceptions and print user friendly output.
"""

from Task7_5 import even_number
import functools
import math


@functools.lru_cache()
def is_prime(number: int) -> bool:
    return math.factorial(number - 1) % number == number - 1


def goldbach(number) -> list:
    if even_number(number):
        int_number = int(number)
        #if int_number == 4:
        #    return [1, 3]

        for p1 in range(3, int_number):
            p2 = int_number - p1
            if is_prime(p1) and is_prime(p2):
                return [p1, p2]


if __name__ == '__main__':
    while True:
        number = input('Enter a number (press "q" to exit)')
    print(goldbach('8'))