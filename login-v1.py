users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

while True:
    user_name = input("User: ")
    password = input("Password: ")

    if user_name in users and users[user_name] == password:
        print()# om key och value är samma i input som i users, printas f-string
        print(f"Welcome {user_name}")
        break # loopen breakeas då det är korrekt.
    else: # Annars... invalid och while loopen börjar om.
        print()
        print("Invalid username or password")
        print()
    
   
            

