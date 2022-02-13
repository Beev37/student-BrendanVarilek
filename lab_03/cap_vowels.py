"""This code propmts the user to enter a sentence, and the output will result in the same
sentence but with the vowels capitalized, and consonants in lower case"""

def case_changer(string):
    """function that takes strings and outputs a new string with the desired modifications"""
    vowels = ['a','e','i','o','u']
    new_string = ""
    for chrctr in string:
        if chrctr not in vowels:
            chrctr = chrctr.lower()
        elif chrctr in vowels:
            chrctr = chrctr.upper()
        new_string = new_string + chrctr

    return new_string
