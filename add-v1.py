"""
ducks = ["Huey", "Dewey", "Louie"]

print(f"List of ducks: {ducks}")
print()

new_duck = input("Add a duck: ")
ducks.append(new_duck)

print()
print(f"Updated list of ducks: {ducks}")
print()
"""

def add(prompt, strings): # prompt är en uppmaning/fråga. strings är en lista.
    new_string = input(prompt) # Nya elementet i listan.
    strings.append(new_string) # lägger till new_string i listan.
    return strings


#Test of the function add with the list ducks.
ducks = ["Huey", "Dewey", "Louie"]

print(f"	Ducks: {ducks}")
print()

ducks_alias = add("		Add a duck: ", ducks)

print()
print(f"	Ducks: {ducks}")
print(f"Alias of Ducks: {ducks_alias}")
print()

#Test of the funtion add with the list composers.

composers = ["Mozart", "Bach"]
print(f"	Composers: {composers}")
print()

add("Add a composer: ", composers)

print()
print(f"	Composers: {composers}")
print()
    
