import sys
import os
from libr import methods
from sys import argv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run(args: list) -> None:
    """
    This function runs the program
    :param args: command line arguments
    :return: None
    """

    file_in, file_out = args[1:]

    if len(args) != 3:
        print("Incorrect command line. Waited: app.py input_file.txt output_file.txt")
        sys.exit()

    container = methods.create_container()

    # Running methods
    methods.read_file(container, file_in)
    methods.write_file(container, file_out)
    methods.clear(container)


if __name__ == '__main__':
    console_args = argv
    run(argv)
