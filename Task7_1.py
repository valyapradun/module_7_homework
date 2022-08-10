"""
Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor.
"""


class File(object):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            print("Exception has been handled")
            print(exception_type)
            print(exception_value)
            print(traceback)
        self.file_obj.close()
        return True


if __name__ == '__main__':
    file_1 = File('./data/lorem_ipsum.txt', 'r')
    file_2 = File('./data/new_file.txt', 'w')
    with file_1 as read_file, file_2 as write_file:
        print(read_file.read())
        #print(read_file.undefined_function())
        print(write_file.write('Hello!'))
        print(write_file.undefined_function('Hello!'))
