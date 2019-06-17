import sys
from uuid import uuid4


def make(number):
    for _ in range(number):
        print(str(uuid4()))


if __name__ == '__main__':
    make(int(sys.argv[1]))
