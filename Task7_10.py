"""
Implement a generator which will generate odd numbers endlessly.
Example:
```python
gen = endless_generator()
while True:
    print(next(gen))
>> 1 3 5 7 ... 128736187263 128736187265 ...
"""


def endless_generator():
    start = 1
    while True:
        yield start
        start += 2


if __name__ == '__main__':
    gen = endless_generator()
    while True:
        print(next(gen))
