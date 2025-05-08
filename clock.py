

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():



    # hardcode

    while True:
        date_choice = input("Date: ")

        if '/' in date_choice and date_choice[0].isalpha():
            continue

        elif ',' in date_choice and date_choice[0:2].isnumeric() and date_choice[5].isalpha():
            continue

        elif ',' in date_choice:
            convert_english_prompt(date_choice)
            break
        elif '/' in date_choice:
            convert_number_prompt(date_choice)
            break

def convert_english_prompt(date):
    # August 14, 2014

    date_prompt = date

    while True:
        new_date = date_prompt.strip()
        new_date = new_date.split(" ")
        month = new_date[0]
        day = new_date[1]
        day = day[0:-1]
        day = int(day)
        year = new_date[2]

        if month in months and (day >= 1 and day <= 31):
            month_number = months.index(month) + 1
            print(f"{year}-{month_number:02}-{day:02}")
            break
        else:
            date_prompt = input("Date: ")
            continue


def convert_number_prompt(date):
    date_prompt = date

    while True:
        new_date = date_prompt.strip()
        new_date = new_date.split("/")
        month = new_date[0]
        month = int(month)
        day = new_date[1]
        day = int(day)
        year = new_date[2]

        if month >= 1 and month <= 12 and (day >= 1 and day <= 31):
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            date_prompt = input("Date: ")
            continue

main()






