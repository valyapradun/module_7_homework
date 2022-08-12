"""
Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
Example:
```python
gen = endless_fib_generator()
while True:
    print(next(gen))
>> 1 1 2 3 5 8 13 ...
```
"""


def endless_fib_generator():
    start = 0
    current = 1
    while True:
        yield start
        start, current = current, start + current


if __name__ == '__main__':
    gen = endless_fib_generator()
    while True:
        print(next(gen))
