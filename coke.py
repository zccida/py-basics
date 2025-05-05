'''
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''


amount_due = 50

while amount_due > 0:
    print(f"Amount due: {amount_due}")
    coin = int(input("Insert coin: "))

    if coin == 5 or coin == 10 or coin == 25:
        amount_due -= coin
    else:
        continue

amount_due = str(amount_due)

if '-' in amount_due:
    amount_due = amount_due[1:]
print("Change Owed: " + amount_due)
