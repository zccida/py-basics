import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    word_input = s
    matches = re.findall(r"\d{1,2}(?::\d{2})? (?:am|pm)", word_input, re.IGNORECASE)
    to_check = re.search(r"\bto\b", word_input, re.IGNORECASE)
    am_pm_check = re.search(r"(am|pm)", word_input, re.IGNORECASE)
    space_check = re.search(r"\d{1,2}(?::\d{2})? (?:am|pm)", word_input, re.IGNORECASE)

    if not to_check:
        sys.exit("ValueError")

    if not space_check:
        sys.exit("ValueError")

    if not am_pm_check:
        sys.exit("ValueError")

    # Check if AM or PM in it



    group_one = matches[0].split(" ")
    group_two = matches[1].split(" ")
    time_one = ""
    time_two = ""



    if ":" in group_one[0]:
        hours_one, minutes_one = group_one[0].split(":")
        hours_one = int(hours_one)
        minutes_one = int(minutes_one)
        if minutes_one >= 60:
            sys.exit("ValueError")
        else:
            time_one = converting_meridem(group_one[1].lower(), hours_one)
            if minutes_one < 10:
                minutes_one = f"0{minutes_one}"
            time_one = f"{time_one}:{minutes_one}"

    elif ":" not in group_one[0]:
        hours_one = group_one[0]
        hours_one = int(hours_one)
        time_one = converting_meridem(group_one[1].lower(), hours_one)
        time_one = f"{time_one}:00"

    if ":" in group_two[0]:
        hours_two, minutes_two = group_two[0].split(":")
        hours_two = int(hours_two)
        minutes_two = int(minutes_two)
        if minutes_two >= 60:
            sys.exit("ValueError")
        else:
            time_two = converting_meridem(group_two[1].lower(), hours_two)
            if minutes_two < 10:
                minutes_two = f"0{minutes_two}"
            time_two = f"{time_two}:{minutes_two}"

    elif ":" not in group_two[0]:
        hours_two = group_two[0]
        hours_two = int(hours_two)
        time_two = converting_meridem(group_two[1].lower(), hours_two)
        time_two = f"{time_two}:00"


    return f"{time_one} to {time_two}"


def converting_meridem(meridem, hours):
     # AM
    if meridem == 'am':
        if hours == 12:
            hours = '00'
            return hours
        elif hours >= 1 and hours <= 9:
            hours = '0' + str(hours)
            return hours
        elif hours == 10 or hours == 11:
            return hours
        else:
            sys.exit("ValueError")

    elif meridem == 'pm':
        if hours == 12:
            return hours
        elif hours >= 1 and hours <= 11:
            hours = hours + 12
            return hours
        else:
            sys.exit("ValueError")
    else:
        sys.exit("ValueError")

if __name__ == "__main__":
    main()
