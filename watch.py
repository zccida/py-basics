import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"iframe src=(\"http\:\/\/|\"https\:\/\/|\"https:\/\/www\.)youtube\.com\/embed\/([a-zA-Z0-9]+)\"", s)
    if match:
        return(f"https://youtu.be/{match.group(2)}")
    else:
        return "None"





if __name__ == "__main__":
    main()
