'''

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Start with 2 letters, min 2 , max 6 length
    # Length Check
    if len(s) < 2 or len(s) > 6:
        return False

    # First two chars = alpha
    if s[0:2].isalpha() == False:
        return False

    if s[0:6].isalpha() == True:
        return True

    # If not digits/alpha

    for char in s:
        if char.isdigit() == False and char.isalpha() == False:
            return False


    # Check if zero is the first number
    zero_check = 0
    for char in s:
        if char.isdigit():
            if char != '0':
                zero_check += 1
            else:
                zero_check -= 1
                if zero_check < 0:
                    return False


    for i in range(len(s)):
        if s[i].isdigit() == True:
            if s[i:-1].isdigit() == True:
                return True
            else:
                return False


main()
