
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
            if option == "1":
                biathlon_game()
                

            elif option == "2":
                flipp_blipp_game()

            elif option == "3":
                print("Pop Quiz kommer vara här!")


            print()
            print("------------------------------------------")
            return option
    
           
        else:
            print()
            print("Invalid option, please try again.")
            print()



# Biathlon game
from random import randint #hämtar funktionen randint, inbyggd i python, slumptal

def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("		Biathlon")
    print()
    print("	   a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

open   = 0 #Globala variabler
closed = 1

def is_open(value): 
    if value == open: #0 alltså inte träffad
        return True
    else:
        return False

def is_closed(value):
    if value == closed: #1 om den är träffad
        return True
    else:
        return False

def new_targets():
    return [open, open, open, open, open] #Lista med målen
    
def close_target(targets, position): #targets = listan (ts) är den listan man skickar
    targets[position] = closed #om man stänger ett target 
    return targets             #returneras den uppdaterade listan för det

def points(targets):
    n = 0
    
    for target in targets:#target=ett mål i taget, targets=hela listan med mål
        if is_closed(target): #avgör om taget är open eller closed.
            n = n + 1 #Lägger till 1 för varje gång vi hittar ett stängt mål
    return n

def targets_to_string(targets):
    result = "" # tom variabel som används i if-satsen
    
    for target in targets:
        if is_closed(target): #om träffad, skrivs 0
            result = result + "0 "
        else:
            result = result + "* " #annars *
            
    return result

def view_targets(targets):
    result = "" #lokal variabel
    for x in range(1,6):
        result = result + str(x) + " "
    
    print()
    print(result)                     #printar ut 1-5 över måltavlorna
    print()
    print(targets_to_string(targets))
    print()
        
def random_hit():
    rand_num = randint(0,1)
    if rand_num == 1: # om 1, är det enn träff
        return True
    else:
        return False #annars miss

def shoot(targets, position):
    hit = random_hit() 
    
    if hit == False: #måste avgöra om miss först
        return "Miss"    #hit == True vilket betyder att det finns två sätt
    elif is_open(targets[position]): #avgör om den är open, om den är det stänger den target.
        close_target(targets, position)
        return "Hit on open target"
    else:
        return "Hit on closed target"
    
def parse_target(string): 
    if string.isnumeric() and len(string) == 1: #numeric avgör om det är heltal
        if int(string) > 0 and int(string) < 6:
            return int(string) - 1 # int returnar ex 1 för att göra den till o tas 1 bort
        else:
            return None
    else:
        return None

def biathlon_game():
        
    splash()
    print("You got 5 shots")
    print()
    ts = new_targets() #skapar nya targets 
    for round in range(1,6): # loop för att det är fem skott
        view_targets(ts)
        target_pos = input(f"Shot nr {round} at: ") #låter spelaren skriva in vilken den vill sikta på.
        print()
        print(shoot(ts, parse_target(target_pos))) #visar vad för typ av träff/miss det blev.
    print()                                        #sjukter target, stringen görs om till index
    view_targets(ts) #visar uppdaterade listan/targets i slutet av de fem skotten.
    print()
    print(f"You hit {points(ts)} of 5 targets") #dina poäng visas i slutet


# Flipp Blipp game
def flippblipp(m):
    if m % 3 == 0 and m % 5 == 0:
        return("flipp blipp")

    elif m % 3 == 0:
        return("flipp")

    elif m % 5 == 0:
        return("blipp")

    else:
        return(m)


def flipp_blipp_game():
    print("------------------------------------------")
    print()
    print("               Flipp Blipp")
    print()
    print("             A guessing game") #kan skrivas med f string senare med användarens namn.
    print()
    print("------------------------------------------")
    print()
    n = 1
    i=0
    print("      ", 1)
    while True:
        n = n + 1
    
        answer = input("Nästa: ")
        correct_answer = flippblipp(n)

        if answer == str(correct_answer): #jämförs spelarens svar.
            i=i+1
        else:
            print()
            print("Fel -", correct_answer)
            print()
            print("Game over")
            print()
            print (f"Score: {i}")
            print()
            break

# Pop Quiz

menu()