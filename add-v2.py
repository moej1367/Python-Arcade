# Definition of the function add.
def add(prompt, strings):# prompt är en uppmaning/fråga, strings är listan.
    new_string = input(prompt)# Nya elementet i listan.
    strings.append(new_string)# lägger till new_string i listan.
    return strings

# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

add(" Add a duck: ", ducks)

print(f" Ducks: {ducks}")
print()

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f" Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f" Composers: {composers}")
print()



