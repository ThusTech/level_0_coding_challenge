def is_vowel(str_input):
    duplicated_vowels = ""
    vowels = ""

    for letter in str_input:
       if letter.lower() in "aeiou":
           duplicated_vowels = duplicated_vowels + str(letter.lower()) +" "
    
    
    for letter in duplicated_vowels:
        if letter not in vowels:
            vowels = vowels + letter +", "
    
    print("Vowels: " + vowels[:-2])

is_vowel('Thulani')
