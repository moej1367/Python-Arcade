
options = {"a":"Add item", "l":"List items", "q":"Log out"} #Ordlista

print("Select an action") 
print()
for (key, value) in options.items(): #mha items() kan man plocka ut nyckel och value.
    print(f"	{key}) {value}")

print()


while True:
    key = input("Option: ")
    if key in options:
        print() #du valde key, sen går in i dictionary och hämtar value mha nyckeln
        print(f"You selected option {key}) {options[key]}")
        break   #{options[key]} går in i ordlistan och plockar fram tillhörande value.
