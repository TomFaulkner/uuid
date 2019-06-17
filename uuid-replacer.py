"""Fake UUID Generator:
Usage:
    python3 uuid-replacer.py name start count

Where:
    name is an exactly eight character string
    start is starting uuid number
    count is number of uuids to generate 
"""
import sys
from uuid import uuid4


def replace(line, offset=0):
    u = str(uuid4())[13:]
    fake = line[:11]
    return fake + u


def generate_fake(name, number):
    if len(str(number)) <= 4:
        if number < 10:
            num_str = f'000{number}'
        elif number < 100:
            num_str = f'00{number}'
        elif number < 1000:
            num_str = f'0{number}'

    return f'{name}-{num_str}-{str(uuid4())[13:]}'


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(__doc__)
    name = sys.argv[1]
    start = int(sys.argv[2])
    count = int(sys.argv[3])
    if len(name) != 8:
        print('That was not 8 characters. Exiting.')
        sys.exit()
    for n in range(count):
        print(generate_fake(name, n+start))

