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
        
strings = [] #Globala variabler
n = 5

print(f"n = {n}") 
print()
for _ in range(n): # _ en variabel som inte används
    prompt = "Lägg till en sträng: "
    add(prompt, strings)
print()
description = f"Du har matat in följande {n} strängar"
view(description, strings)
    



