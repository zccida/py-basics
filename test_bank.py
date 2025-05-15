from bank import value

def test_hello():
    assert value('hello world') == 0
    assert value('hello') == 0

def test_h():
    assert value('hi whats up man') == 20
    assert value('hvdasfafnirweiinvf') == 20

def test_cases():
    assert value('Hi man!') == 20
    assert value('HELLO MAN!') == 0

def test_anything():
    assert value(' ') == 100
    assert value('well well well look we have here') == 100

def main():

    output = input("Greeting: ").lower()
    output = output.lower()
    number = value(output)
    print(f"${number}")


# bank file
# def value(greeting):

#     if 'hello' in greeting:
#         number = 0
#     elif 'h' in greeting[0]:
#         number = 20
#     else:
#         number = 100

#     return number


# if __name__ == "__main__":
#     main()
