users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

print("Användare:")
print()
for key in users:
    print(key)

#-----------------------------------------------
print()
print("Användare och lösenord:")
print()
for key in users:
    print(f"{key}) {users[key]}")

#------------------------------------------------
data = {"nisse":["luva", "vante"],
        "bosse":["spik", "skruv", "hammare"],
        "stina":["tidsmaskin"]}

print()
print("Användare och deras data:")
print()
for key in data:
    print(f"{key}) {data[key]}")

#------------------------------------------------
print()
# user_name är samma som key
user_name = input("Slå upp användare: ")
if user_name in data:
    print()# om key finns i data printa nedanstående.
    print(f"Data lagrat för {user_name}: {data[user_name]}")
else:
    print()
    print(f"Användaren {user_name} finns inte")

#------------------------------------------------
