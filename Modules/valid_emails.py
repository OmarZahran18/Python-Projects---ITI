def filter_valid_emails():
    domines = [
        "ali@gmail.com", "sara@yahoo.com",
        "mohamed@outlook.com", "omar@",
        "zahran.yahoo@com", "ahmed.com@gmail",
        "sayed@outlookcom", "khaled hotmail@"
    ]
    valid_emails = filter(
        lambda e: "@" in e and "." in e.split("@")[-1] and e[0] != "@" and e[-1] != "@",
        domines
    )
    print(list(valid_emails))
    
def check_email_attempts():
    def email_validator(email):
        if "@" in email and ".com" in email:
            if email[0] != "@" and email[-1] != "@" and email[-4:] == ".com":
                s = email.split("@")
                if len(s) == 2 and s[1].count(".") <= 1 and s[1].split(".")[0] != "":
                    return True
        return False

    for i in range(5):
        try:
            email = input("Enter your Email: ").strip()
            if email_validator(email):
                print("Valid Email")
                break
            else:
                raise ValueError("Invalid Email")
        except ValueError as e:
            print(e)
    else:
        print("Too many failed attempts. Try again later.")