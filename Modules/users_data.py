def get_user_data():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            break
        else:
            print("Invalid name. Please enter letters only.")
    
    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email. Please try again.")

    print("\nYour data:")
    print("Name:", name)
    print("Email:", email)


def check_user_login():
    users = [
        {"name": "omar", "pass": "123"},
        {"name": "ahmed", "pass": "456"}
    ]
    name = input("Enter your name: ").lower()
    password = input("Enter your password: ")
    for i in users:
        if i["name"] == name and i["pass"] == password:
            print("Valid")
            break
    else:
        print("Invalid")