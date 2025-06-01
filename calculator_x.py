import sys

class Calculator:

    def __init__(self):
        self._result = 0

    def add(self, a):
        self._result += a

    def subtract(self, a):
        self._result -= a

    def multiply(self, a):
        self._result *= a

    def divide(self, a):
        self._result /= a

    @property
    def result(self):
        return self._result

calculator = Calculator()

def check_operand(operand, x):
    if operand == '+':
        calculator.add(x)
    elif operand == '-':
        calculator.subtract(x)
    elif operand == '*':
        calculator.multiply(x)
    elif operand == '/':
        calculator.divide(x)
           

def main():

    print("Welcome to the CALCULATOR!!")
    
    display_screen = ""
    hold_var = ""

    while True:
        x = float(input("Enter a number: "))
        display_screen = display_screen + str(x) + " "
        print(display_screen)
        operand = input("Enter an operand between '+', '-', '*', '/', 'exit' : ")
        

        display_screen = display_screen + operand
        display_screen += " "
        print(display_screen)

        if not operand == 'exit':
            check_operand(operand, x)
            hold_var = operand
        else:
            check_operand(hold_var, x)
            sys.exit(f"Exiting out: {calculator.result}")



if __name__ == "__main__":
    main()
