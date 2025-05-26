from datetime import date
from datetime import timedelta
import sys
import inflect


'''
Prompt the users birth in YYYY-MM-DD format
Print how old they are in minutes rounded to nearest int
Assume that the user was born on midnight that day. ie 00:00:00
Assume that the current time is also midnite
'''

def main():


    input_date = input("Date of birth: ")
    if not "-" in input_date:
        sys.exit("Invalid date")
    words_split = input_date.split("-")

    # Replace the 0's for 01-09
    for word in words_split:
        if word[0] == '0':
            new_word = word.replace('0', '')
            words_split.insert(words_split.index(word),new_word)
            words_split.remove(word)


    # Create a date with them
    new_date = create_date(words_split)
    current_date = date.today()
    total_date = current_date - new_date

    real_minutes = get_minutes(total_date.days)

    p = inflect.engine()
    number_words = p.number_to_words(real_minutes, andword="")


    # Create a sentence
    new_word = ""
    for x in range(len(number_words)):
        if x == 0:
            new_word += number_words[0].upper()
        else:
            new_word += number_words[x]

    print(new_word, "minutes")

def create_date(words_split):
    new_date = date(int(words_split[0]), int(words_split[1]), int(words_split[2]))
    return new_date

def get_minutes(days):
    return days * 60 * 24


if __name__ == "__main__":
    main()
