def main():
    nmbrs = []
    while True:
        usr_in = input("Enter a value to add (no commas, and enter nothing to sum): ")
        if usr_in == "":
            break     
        nmbrs.append(float(usr_in))

    print("The sum of the list is:", sum(nmbrs))
    return sum(nmbrs)

main()