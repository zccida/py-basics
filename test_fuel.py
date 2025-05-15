# '''

# if 1% or less it is E
# if 99% or more it is F

# if x or y is not an integer ValueError
# x is greter than y ValueError
# or y is 0      ZeroDivisionError
# '''

# # convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
# # and returns that fraction as a percentage rounded to the nearest int between 0 and 100,
# # inclusive. If X and/or Y is not an integer, or if X is greater than Y,
# # then convert should raise a ValueError. If Y is 0, then convert should raise a
# # ZeroDivisionError.

# # gauge expects an int and returns a str that is:
# # "E" if that int is less than or equal to 1,
# # "F" if that int is greater than or equal to 99,
# # and "Z%" otherwise, wherein Z is that same int.


# def main():

#     frac = input("Fraction: ")
#     x = convert(frac)

#     t = gauge(x)
#     print(t)

# def convert(fraction):

#     expression = fraction.split("/")

#     if (int(expression[0].isdigit()) and int(expression[1].isdigit())):
#         x = int(expression[0])
#         y = int(expression[1])
#         if y == 0:
#             raise ZeroDivisionError
#         elif x > y:
#             raise ValueError
#         else:
#             return round((x/y) * 100)
#     else:
#         raise ValueError



# def gauge(percentage):

#     percentage = int(percentage)

#     if percentage <= 1:
#         return 'E'
#     elif percentage >= 99:
#         return 'F'
#     else:
#         return f"{percentage}%"

# if __name__ == "__main__":
#     main()




// test 

from fuel import convert, gauge
import pytest

def test_convert_original():
    assert convert('3/5') == 60
    assert convert('2/4') == 50

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')

def test_convert_value():
    with pytest.raises(ValueError):
        convert('3/1')

def test_gauge_e():
    assert gauge(1) == 'E'

def test_gauge_f():
    assert gauge(99) == 'F'

def test_gauge_zero():
    assert gauge(0) == 'E'

def test_gauge_else():
    assert gauge(66) == '66%'



