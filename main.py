def ask():
    is_alpha = True
    while is_alpha:
        yes_no = input("Value : ")
        if yes_no.lower() == "yes":
            is_alpha = False
            return True
        elif yes_no.lower() == "no":
            is_alpha = False
            return False
        else:
            print("Please, Enter yes or no only")
