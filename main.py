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
    is_loop = True
while is_loop:
    print("Welcome, MC identifier program")
    print("Uploaded on time?")
    if ask():
        print("Full mark")
    else:
        print("uploaded in 24 hours?")
        if ask():
            print("Late submission")
            print("is there valid reason?")
            if ask():
                print("MC")
                print("Is Accepted")
                if ask():
                    print("Full mark")
                else:
                    print("minus 10 mark if mark is above 40")
            else :
                print("minus 10 mark if mark is above 40")
        else:
            print("uploaded within 5 days")
            if ask():
                print("Valid reason?")
                if ask():
                    print("MC (late submission option)")
                    print("Accepted?")
                    if ask():
                        print("Full mark")
                    else:
                        print("Zero Mark (0)")
                else:
                    print("Zero Mark (0)")
            else:
                print("Valid reason?")
                if ask():
                    print("MC(non -submission/deferral before specified deadline)")
                    print("Accepted, push to deferral reassessment")
                else:
                    print("Zero Mark (0)")
    print("Want to do again?")
    if ask():
        is_loop = True
    else:
        is_loop = False