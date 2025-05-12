import random
import sys


def main():

    while True:

        level = input("Level: ")

        if level.isdigit() == True and int(level) > 0:
            break


    random_number = random.randint(1, int(level))


    while True:

        guess = input("Guess: ")
        if guess.isdigit() == True:
            guess = int(guess)

            if guess < random_number:
                print("Too Small!")
            elif guess > random_number:
                print("Too Large!")
            else:
                sys.exit("Just Right!")
    
main()
