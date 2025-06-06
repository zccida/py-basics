'''

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
'''

import sys
import csv

def main():

    people = []
    new_people = []


    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    people.append({"name": row["name"], "house": row["house"]})

            for person in people:
                names = person["name"].split()
                last = names[0].replace(",", "")
                first = names[1]
                new_people.append({"first": first, "last": last, "house": person["house"]})

            with open(sys.argv[2], 'w') as output_file:
                writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for person in new_people:
                    writer.writerow({"first": person["first"], "last": person["last"], "house": person["house"]})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
