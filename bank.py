

'''
If 'hello' in greeting, return 0$
If greeting starts with a 'h' return 20$
If anything else, $100
'''

output = input("Greeting: ").lower()
number = 0

if 'hello' in output:
    number = 0
elif 'h' in output[0]:
    number = 20
else:
    number = 100

print(f"${number}")
