vowels = 'AEIOUaeiou'


user_input = input("Input: ")
user_output = ""

for letter in user_input:
    if letter not in vowels:
        user_output += letter

print(f"Output: {user_output}")

