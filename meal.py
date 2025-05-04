def main():


    time_input = input("What time is it? ")
    time_input = convert(time_input)



    if time_input >= 7 and time_input <= 8:
        print("breakfast time")
    elif time_input >= 12 and time_input <= 13:
        print("lunch time")
    elif time_input >= 18 and time_input <= 19:
        print("dinner time")


def convert(time):

    # 7:00 - 8:00 Breakfast
    # 12:00 - 13:00 Lunch
    # 18:00 - 19:00 Dinner

    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    total_time = hours + minutes
    total_time = float(total_time)
    return total_time



if __name__ == "__main__":
    main()
