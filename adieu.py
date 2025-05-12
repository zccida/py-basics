names = []
sentence = "Adieu, adieu, to "

while True:


    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

if len(names) > 2:
    for i in range(len(names)):
        if i != len(names) - 1:
            names[i] = names[i] + ","

if len(names) > 1:
    names.insert(len(names)-1, 'and')

for name in names:
    sentence += name + " "


print(sentence)
