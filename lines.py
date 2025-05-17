import sys

'''
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines. If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
'''


def main():

    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], "r") as file:
                print(file)
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
