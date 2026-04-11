def food(t):
    hours, minutes = t.split(":")
    return int(hours) + int(minutes) / 60


try:

    user_time = input("what time is it right now?? ")

    t= food(user_time)

    if 6<=t<=8:
        print("breakfast time")

    elif 12<=t<=14:
        print("lunch time")

    elif 18<=t<=20:
        print("dinner time")

    elif t>24 or t<0:
        print("invalid time")
    else:
        print("snack time")

except ValueError:
    print("Please enter time in the format HH:MM")
