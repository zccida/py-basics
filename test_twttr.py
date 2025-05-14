# twttr file
# vowels = 'AEIOUaeiou'
# def main():

#     user_input = input("Input: ")
#     shortened_word = shorten(user_input)
#     print(f"Output: {shortened_word}")

# def shorten(word):
#     user_output = ""

#     for letter in word:
#         if letter not in vowels:
#             user_output += letter

#     return user_output


# if __name__ == "__main__":
#     main()


import pytest
from twttr import shorten



def test_shorten_uppercase():
    assert shorten("REAL WORLD") == "RL WRLD"

def test_shorten_lowercase():
    assert shorten("hello world") == "hll wrld"

def test_shorten_both():
    assert shorten("HELLO world") == "HLL wrld"

def test_shorten_nums():
    assert shorten("what1 up") == "wht1 p"

def test_shorten_punctuation():
    assert shorten("well. its. like. what?") == "wll. ts. lk. wht?"
