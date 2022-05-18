def convert_to_time(x):
    hour = x // 60
    min = x % 60

    if hour > 1:
        if min > 1:
            print(f"{hour} hours,{min} minutes")
        elif min == 1:
            print(f"{hour} hours,{min} minute")
        else:
            print(f"{hour} hours,{min:02d} minute")
    elif hour <= 1:
        if min > 1:
            print(f"{hour} hour,{min} minutes")
        elif min == 1:
            print(f"{hour} hour,{min} minute")
        else:
            print(f"{hour} hour,{min:02d} minute")

convert_to_time(120)
