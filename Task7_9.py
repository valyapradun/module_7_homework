"""
Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments
and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
_Note: Do not use function `range()` at all_
Example:
```python
er1 = EvenRange(7,11)
next(er1)
>> 8
next(er1)
>> 10
next(er1)
>> "Out of numbers!"
next(er1)
>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
>> 4 6 8 10 12 "Out of numbers!"
"""


class EvenRange:

    def __init__(self, start, end):
        if start % 2 == 0:
            self.start = start
        else:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration('Out of numbers!')
        current = self.start
        self.start += 2
        return current


if __name__ == '__main__':
    er1 = EvenRange(7, 11)
    print(next(er1))
    print(next(er1))
    #print(next(er1))
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
