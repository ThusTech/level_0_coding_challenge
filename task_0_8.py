def convert_to_time(number):
    hour = number // 60
    minute = number % 60

    if hour > 1 or hour == 0:
        if minute > 1 or minute == 0:
            print(f"{hour} hours,{minute} minutes")
        elif minute == 1:
            print(f"{hour} hours,{minute} minute")
    elif hour == 1:
        if minute > 1 or minute == 0:
            print(f"{hour} hour,{minute} minutes")
        elif minute == 1:
            print(f"{hour} hour,{minute} minute")
convert_to_time(1)
