import re

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    x = len(matches)
    return x


if __name__ == "__main__":
    main()
