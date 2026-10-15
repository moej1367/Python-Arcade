
games = {"1":"Biathlon", "2":"Flipp Blipp", "3":"Pop Quiz"}

def menu():
    print("------------------------------------------")
    print()
    print("             Python Arcade")
    print()
    print("                Welcome!") #kan skrivas med f string senare med användarens namn.
    print()
    print("------------------------------------------")
    print()

    for (key, value) in games.items():
        print(f"            {key}) {value}")
        print()

    while True:
        option = input("Option: ")
        if option in games:
            print()
            return option
        else:
            print()
            print("Invalid option, please try again.")
            print()
    
    print("------------------------------------------")



menu()


