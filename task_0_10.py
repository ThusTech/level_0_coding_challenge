def common_letter(first_string, second_string):
    common = ""
    list_of_strings = list(set(first_string)&set(second_string))

    for letter in list_of_strings:
        common = common + str(letter.lower()) + ", "

    print("Common letters: "+ common[:-2])


common_letter("House","computHers")