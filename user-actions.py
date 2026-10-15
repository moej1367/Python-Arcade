
def add(prompt, strings):
    new_string = input(prompt)
    strings.append(new_string)
    return strings

def view(description, strings):
    print(description)
    print()
    rad_num = 1
    for string in strings:
        print(f"{rad_num}) {string}")
        rad_num += 1
        

def menu(title, prompt, options):
    print(title)
    print()
    for (key, value) in options.items():
        print(f"	{key}) {value}")

    print()

    while True:
        key = input(f"{prompt}: ")
        if key in options:
            print()
            return key
        
def user_actions(user, items):
    options = {"a":"Add item",
               "l":"List items",
               "q":"Log out"}

    print(f"Welcome {user}")
    print()
    while True:
        view("These are your items", items)
        print()
        answer = menu("Select an action", "Option", options)
        if answer == "a":
            add("Add item: ", items)
            print()
        elif answer == "l":
            print()
            view("These are your items", items)
        elif answer == "q":
            return(items)
        
        
    


user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]

user_actions(user1, items1)
print(f"Goodbye {user1}, your items: {items1}")
print()

user_actions(user2, items2)
print(f"Goodbye {user2}, your items: {items2}")
print()