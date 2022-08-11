"""
Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.
"""

from contextlib import contextmanager


@contextmanager
def file_open(path, mode):
    try:
        file_obj = open(path, mode)
        yield file_obj
    except Exception as exc:
        print("We had an error!")
        print(exc.__str__())
    finally:
        print('Closing file')
        file_obj.close()


if __name__ == '__main__':
    with file_open('./data/lorem_ipsum.txt', 'r') as read_file:
        print(read_file.read())
    with file_open('./data/new_file.txt', 'w') as write_file:
        print(write_file.write('Hello2!'))
        print(write_file.undefined_function('Hello2!'))