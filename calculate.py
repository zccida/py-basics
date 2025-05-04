'''

In a file called interpreter.py, implement a program that
prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

+
-
/
*

y becomes our operand
x z becomes our a b
'''


some_str = input("Expression: ")
x, y, z = some_str.split(" ")
x = float(x)
z = float(z)

def calc(x, y, z):
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '/':
        return x / z
    else:
        return x * z

result = calc(x, y , z)
print(f"{result:.1f}")
