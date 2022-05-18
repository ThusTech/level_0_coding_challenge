def maximum_number(*arguments):
    max_number = arguments[0]

    for i in arguments:
        if i > max_number:
            max_number=i
    return max_number

print(str(maximum_number(10,2,3,4)))