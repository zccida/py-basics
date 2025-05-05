'''
Make a snakecase for camelcase words
'''


word = input("camelCase: ")
new_word = ""
for letter in word:
    if letter.isupper():
        new_word += "_"
        new_word += letter.lower()
    else:
        new_word += letter

print("snake_case: " +  new_word)
