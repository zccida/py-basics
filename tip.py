'''
This program receives a $str input , turn it to float, and calculates the tip percentage for you
'''

def main():

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO

    # get a string, remove the $ and return it as a float
    d = d.replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):
    # TODO

    p = p.replace("%", "")
    p = float(p)
    p = p / 100
    return p


main()
