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
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1], "r") as file:
                    count = read_file(sys.argv[1])
                    print(count)
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")


def read_file(file_name):
    counter = 0
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            if len(line) == 0 or line.startswith('#'):
                continue
            else:
                counter = counter + 1

    return counter
if __name__ == "__main__":
    main()
