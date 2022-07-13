from pathlib import Path
import sys
p = Path(sys.argv[1])


def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f'This is folder - {element.name}')
            parse_folder_recursion(element)
        else:
            print(f'This is file - {element.name}')


if __name__ == '__main__':
    parse_folder_recursion(p)
