def view(description, strings):
    print(description)
    print()
    rad_num = 0 #rad_nummer = radens nummer
    for string in strings: #string är ett element i listan.
        rad_num += 1  #rad_num += 1   betyder att du ökar med HL på VL
        print(f"{rad_num}) {string}")
    

names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)