

grocery_list = {}



while True:
    try:
        grocery_input = input("").lower()
        if grocery_input not in grocery_list:
            grocery_list.update({grocery_input : 1})
        else:
            num = grocery_list[grocery_input]
            grocery_list[grocery_input] = num + 1
    except EOFError:
        break

print()

sorted_list = sorted(grocery_list.keys())


for item in sorted_list:
    print(f"{grocery_list[item]} {item.upper()}")
