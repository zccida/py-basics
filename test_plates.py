from plates import is_valid


def test_length():
    assert is_valid('C') == False
    assert is_valid('COCONONO') == False
    assert is_valid('coco') == True


def test_two_chars():
    assert is_valid('AB') == True
    assert is_valid('A1') == False

def test_numbers():
    assert is_valid('CS50AB') == False
    assert is_valid('CSAB50') == True

def test_zeros():
    assert is_valid('CS05') == False
    assert is_valid('CS50') == True

def test_non_alpha_numeric():
    assert is_valid('AB!@50') == False
    assert is_valid('!?@_') == False
    




# // 

# '''

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

# '''

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):

#     # Start with 2 letters, min 2 , max 6 length
#     # Length Check
#     if len(s) < 2 or len(s) > 6:
#         return False

#     # First two chars = alpha
#     if s[0:2].isalpha() == False:
#         return False

#     if s[0:6].isalpha() == True:
#         return True

#     # If not digits/alpha

#     for char in s:
#         if char.isdigit() == False and char.isalpha() == False:
#             return False


#     # Check if zero is the first number
#     zero_check = 0
#     for char in s:
#         if char.isdigit():
#             if char != '0':
#                 zero_check += 1
#             else:
#                 zero_check -= 1
#                 if zero_check < 0:
#                     return False


#     for i in range(len(s)):
#         if s[i].isdigit() == True:
#             if s[i:-1].isdigit() == True:
#                 return True
#             else:
#                 return False


# if __name__ == "__main__":
#     main()
