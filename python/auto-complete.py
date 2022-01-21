import os
from queue import Empty


def file_is_exist(file) -> bool :
    return os.path.exists(file)

def file_is_empty(file) -> bool :
    return os.path.getsize(file)

def main(file):
    os.chdir('/home')
    print(os.getcwd())
    print(file_is_exist(file))
    print(file_is_empty(file))


if __name__ == '__main__':
    main("/Users/sunlei/.bashrc")