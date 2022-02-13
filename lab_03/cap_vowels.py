"""This code propmts the user to enter a sentence, and the output will result in the same
sentence but with the vowels capitalized, and consonants in lower case"""
def main():
    """Creates a function to manipulate the string properly and then, later, requests an
    input from the user for the created function to operate on."""
    def case_changer(string):
        """function that takes strings and outputs a new string with the desired modifications"""
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        new_string = ""
        for chrctr in string:
            if chrctr.upper() and chrctr.lower() not in vowels:
                chrctr = chrctr.lower()
            elif chrctr.upper() and chrctr.lower() in vowels:
                chrctr = chrctr.upper()
            new_string = new_string + chrctr

        print(new_string)
        return new_string

    usr_in = input("Enter a sentence to be modified: ")
    case_changer(usr_in)

main()
