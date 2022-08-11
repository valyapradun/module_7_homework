"""
Implement decorator with context manager support for writing execution time to log-file.
See contextlib module.
"""
from contextlib import ContextDecorator
import time


class DecoratorContextManager(ContextDecorator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_file = None
        self.start_time = None
        self.end_time = None

    def start_work(self):
        self.log_file = open('./data/new_file.txt', 'a')
        self.start_time = time.time()

    def end_work(self):
        self.end_time = time.time()
        try:
            self.log_file.write(f'\nExecution time: {self.end_time - self.start_time}')
        except Exception as exc:
            print("We had an error!")
            print(exc.__str__())
        finally:
            print('Closing file')
            self.log_file.close()

    def __enter__(self):
        self.start_work()

    def __exit__(self, exception_type, exception_value, traceback):
        self.end_work()


@DecoratorContextManager()
def test():
    print('Starting execution...')
    time.sleep(5)
    print('Ending execution...')


if __name__ == '__main__':
    test()