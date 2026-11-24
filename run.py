import multiprocessing
import sys
from pys import cyrus


def exception_handler(exception_type, exception, traceback):
    del traceback
    print("Sorry, an error occurred in the tool. Please submit the following log to the developer:")
    sys.stderr.write('{}: {}\n'.format(exception_type.__name__, exception))
    if input("Restart? [1=Restart/0=Exit]: ") == "1":
        init()
    else:
        sys.exit(1)


def init():
    cyrus.check_permissions()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    sys.excepthook = exception_handler
    init()
