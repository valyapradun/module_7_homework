"""
Implement your custom iterator class called MySquareIterator
which gives squares of elements of collection it iterates through.
Example:
```python
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
>> 1 4 9 16 25
```
"""


class MySquareIterator(object):
    def __init__(self, lst):
        self.num = 0
        self.lst = list(lst)
        self.stop = len(self.lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.stop:
            raise StopIteration
        res = self.num ** 2
        self.num += 1
        return res

    def __str__(self):
        return str(list(self))


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)

    itr = MySquareIterator('12345')
    for item in itr:
        print(item)

