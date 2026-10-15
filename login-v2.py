def login(users):
    while True:
        user_name = input("User: ")
        password = input("Password: ")

        if user_name in users and users[user_name] == password:
            print()
            return user_name #skickar tillbaks username utanför funktionen
           
        else:
            print()
            print("Invalid username or password")
            print()

users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user1 = login(users1)
print(f"Welcome {user1}")
print()
users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")