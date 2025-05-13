import random

# Prompts the user for a level, If the user does not input 1, 2, or 3, the program should prompt again.


#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with N
# digits. No need to support operations other than addition (+).

# Prompts the user to solve each of those problems.
# If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
# allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries,
# the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.


def main():


    # Start of the game
    level = get_level()

    score = 0
    problems = 10

    while True:
        if problems > 0:
            problems = problems - 1
            guess = 0

            x = generate_integer(level)
            y = generate_integer(level)

            while True:
                if guess != 3:
                    math_input = input(f"{x} + {y} = ")
                    if math_input.isdigit() and int(math_input) == (x+y):
                        score = score + 1
                        break
                    else:
                        print("EEE")
                        guess = guess + 1

                elif guess == 3:
                    print(f"{x} + {y} = {x+y}")
                    break

        else:
            break

    print(f"Score: {score}")



def get_level():

    while True:
        level = input("Level: ")
        if level.isdigit():
            if int(level) >= 1 and int(level) <= 3:
                break

    return int(level)



def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        return 0

if __name__ == "__main__":
    main()
