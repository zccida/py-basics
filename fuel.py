'''

if 1% or less it is E
if 99% or more it is F

if x or y is not an integer ValueError
x is greter than y ValueError
or y is 0      ZeroDivisionError
'''


while True:
    frac = input("Fraction: ")

    try:
        expression = frac.split("/")
        x = int(expression[0])
        y = int(expression[1])
        x / y

    except ValueError:
        print("ValueError")

    except ZeroDivisionError:
        print("ZeroDivisionError")

    else:
        if x > y:
            print("ValueError")
            continue
        else:
            new_percentage = x / y
            new_percentage *= 100
            new_percentage = round(new_percentage)
            message = f"{round(new_percentage)}%"

            if new_percentage >= 99:
                print("F")
            elif new_percentage <= 1:
                print("E")
            else:
                print(message)
            break
