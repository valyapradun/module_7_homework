"""
Implement your custom collection called MyNumberCollection.
It should be able to contain only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised.
Method init sholud be able to take either `start,end,step` arguments, where
`start` - first number of collection,
`end` - last number of collection or some ordered iterable collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
>> [0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5,))
print(col2)
>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
>> [0, 2, 4, 5, 7]
col2.append("string")
>> TypeError: 'string' - object is not a number!
print(col1 + col2)
>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
>> [0, 2, 4, 5, 7]
print(col2)
>> [1, 2, 3, 4, 5]
print(col2[4])
>> 25
for item in col1:
    print(item)
>> 0 2 4 5 7
```
"""


class MyNumberCollection(object):

    @staticmethod
    def is_number(item):
        if isinstance(item, int):
            return item
        else:
            raise TypeError('MyNumberCollection supports only numbers!')

    def __init__(self, *args):
        if len(args) == 1:
            self.elements = [self.is_number(item) for item in args[0]]
        else:
            self.elements = list(range(*args))
            self.elements.append(args[1])

    def __iter__(self):
        self.start_index = 0
        return self

    def __next__(self):
        if self.start_index > len(self.elements):
            raise StopIteration
        current = self.start_index
        self.start_index += 1
        return current

    def __str__(self):
        return str(self.elements)

    def __add__(self, other):
        return MyNumberCollection(self.elements + other.elements)

    def __getitem__(self, item):
        return self.elements[item] ** 2

    def append(self, item):
        if isinstance(item, int):
            self.elements.append(item)
        else:
            raise TypeError("'string' - object is not a number!")


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5,))
    print(col2)
    #col3 = MyNumberCollection((1, 2, 3, "4", 5))
    col1.append(7)
    print(col1)
    #col2.append("string")
    print(col1 + col2)
    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item)
