
def menu(prompt, options): 
    print()
    for (key, value) in options.items():
        print(f"	{key}) {value}")

    print()

    while True:
        key = input(f"{prompt}: ")
        if key in options:
            print()
            return key

def login(users):
    while True:
        user_name = input("User: ")
        password = input("Password: ")

        if user_name in users and users[user_name] == password:
            print()
            return user_name #skickar tillbaks username
           
        else:
            print()
            print("Invalid username or password")
            print()
            answer = menu("Option", options) # Ger nya val, r eller q
            if answer == "q":
                return None
        
options = {"r":"Try again", "q":"Quit"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user = login(users)