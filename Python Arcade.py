

def login_splash():
    print("------------------------------------------")
    print()
    print("             Python Arcade")
    print()
    print("                Welcome!")
    print()
    print("------------------------------------------")
    print()
   
def menu(prompt, options): 
        print()

        for (key, value) in options.items(): #Radar upp valen man har, använder items för att 
            print(f"	{key}) {value}")#plocka ut key och motsvarande value

        print()

        while True:
            key = input(f"{prompt}: ")#key är det alternativet man skriver in

            if key in options: #om key finns i dictionary options returnas svaret man skrev in
                print()
                return key

def login(users):
        options = {"r":"Try again", "q":"Quit"}

        while True:
            print("         Log in to your account")
            print()
            user_name = input("User: ")
            password = input("Password: ")

            if user_name in users and users[user_name] == password: #Om username OCH lösen stämmer returnas username
                print()
                return user_name #skickar tillbaks username
            
            else:
                print()
                print("Invalid username or password")
                print()
                answer = menu("Option", options) # Ger nya val, r eller q #funktion menu anropas
                
                if answer == "q":
                    return None
    

#-------------------------------------------------------------------------------------------------------------------#

games = {"1":"Biathlon", "2":"Flipp Blipp", "3":"Pop Quiz"}

def main_menu(user_name):
    biathlon_score = 0
    flipp_blipp_score = 0
    pop_quiz_score = 0

    while True:
        print("------------------------------------------")
        print()
        print("             Python Arcade")
        print()
        print(f"             Welcome {user_name}!") 
        print()
        print("------------------------------------------")
        print()
        print("         Choose a game to play")
        print()

        for (key, value) in games.items():
            print(f"            {key}) {value}")
            print()
        print("            4) Log out")
        print()

        option = input("Option: ") #man väljer alternativ

        if option == "4":
            print()
            print("================ SCOREBOARD ================")
            print()
            print(f"Player: {user_name}")
            print()
            print("                  Scores:")
            print(f"Biathlon: {biathlon_score}")
            print()
            print(f"Flipp Blipp: {flipp_blipp_score}")
            print()
            print(f"Pop Quiz: {pop_quiz_score}")
            print()
            print("============================================")
            print()
            print(f"Goodbye, {user_name}!")
            print()
            return "logout" #logout sparas som en variabel för vilket val användaren gjorde
        
        elif option in games:
            if option == "1":
                game = biathlon_game 

            elif option == "2":
                game = flipp_blipp_game #sparar en referens till spelets funktion

            elif option == "3":
                game = pop_quiz_game

            

            while True:
                score = game() #startar själva spelet som väljs och sätter en referens i form av score

                if option == "1":
                    biathlon_score += score #sätter att score som returnar
                elif option == "2":         #från funk blir spelet_score som variabel
                    flipp_blipp_score += score
                elif option == "3":
                    pop_quiz_score += score

                print()
                print("------------------------------------------")
            
                choice = after_game() #när spelet är slut anropas after_game().
                if choice == "menu":
                    break
        
            
        else:
            print()
            print("Invalid option, please try again.")
            print()



def after_game():
    print()
    print("What would you like to do?")
    print()
    print("1) Play again")
    print()
    print("2) Main menu")
    print()

    while True:
        option = input("Option: ")
        print()
        if option == "1": #om spelare väljer 1 returnerar funktion replay. Den inre loopen börjar om och spelet körs igen.
            return "replay" 
        elif option == "2": #om spelare väljer 2 returnerar funk menu. break avslutar den inre loopen
            return "menu"   #och den yttre loopen visar huvudmenyn igen.
        else:
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

def points_bi(targets):
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
    print(f"You hit {points_bi(ts)} of 5 targets") #dina poäng visas i slutet
    return int(points_bi(ts))


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
    print()
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
            return i
            break

# Pop Quiz

import random
import time 

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("		Pop Quiz")
    print()
    print("      Test your all-around knowledge "   )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")       

def pop_quiz(question, prompt, options, correct_answer):
    print()
    print(question)
    print()
    for(key, value) in options.items():
        print(f" {key}) {value}")
    print()
    
    while True:
        answer=input(f" {prompt}: ")
        if answer in options:
            print()
            if answer== correct_answer:
                print (" Correct!")
                print("_________________________")
                time.sleep(0.5)
                print()
                return answer
            else:
                print (" Incorrect!")
                print("_________________________")
                print()
                time.sleep(0.5)
                return answer
        else:
            print()
            print("Invalid answer, please try again!")
            print()
          
options_1={"A":"Sea turtles", "B":"Octopus", "C":"Dolhpin", "D":"Shark"}

options_2={"A":"Nintendo", "B":"Microsoft", "C":"Sega", "D":"Sony"}

options_3={"A":"Sydney", "B":"Melbourne", "C":"Brisbane", "D":"Canberra"}

options_4={"A":"1989", "B":"1991", "C":"1987", "D":"1993"}

options_5={"A":"Ag", "B":"Fe", "C":"gd", "D":"Au"}

options_6={"A":"184", "B":"215", "C":"206", "D":"230"}

options_7={"A":"George Lucas", "B":"Peter Jackson", "C":"Steven Spielberg", "D":"James Cameron"}

options_8={"A":"Norway", "B":"Canada", "C":"Sweden", "D":"Finland"}

options_9={"A":"Rosalind Franklin", "B":"Marie Curie", "C":"Ada Lovelace", "D":"Lise Meitner"}

options_10={"A":"1912", "B":"1905", "C":"1920", "D":"1918"}

options_11={"A":"Pink", "B":"White", "C":"Brown", "D":"Black"}

options_12={"A":"Koala", "B":"Sloth", "C":"Chimpanzee", "D":"Raccoon"}

options_13={"A":"A colony", "B":"A flotilla", "C":"A flamboyance", "D":"A festival"}

options_14={"A":"France", "B":"Belgium", "C":"United States", "D":"United Kingdom"}

options_15={"A":"Sonic the Hedgehog", "B":"Pac-Man", "C":"Mario", "D":"Mega Man"}


def random_questions():
    questions=[
    ("Which animal has three hearts?", "Your answer ", options_1, "B"),
    ("Which company created the PlayStation?", "Your answer ", options_2, "D"),
    ("Which is the capital of Australia?", "Your answer ", options_3, "D"),
    ("Which year did the Berlin Wall fall?", "Your answer ", options_4, "A"),
    ("What is the chemical symbol for gold?", "Your answer ", options_5, "D"),
    ("How many bones does an adult human have in their body normally?", "Your answer ", options_6, "C"),
    ("Who directed the films 'Lord of the rings'?", "Your answer ", options_7, "B"),
    ("Which country has the most islands ?", "Your answer ", options_8, "C"),
    ("Who was the first woman to win a Nobel Prize in 1903 ?", "Your answer ", options_9, "B"),
    ("Which year did the Titanic sink on its maiden voyage?", "Your answer ", options_10, "A"),
    ("What color is a polar bear's skin underneath their white fur?", "Your answer ", options_11, "D"),
    ("Which animal has remarkably similar finger prints to a human?", "Your answer ", options_12, "A"),
    ("What is a group of flamingos called?", "Your answer ", options_13, "C"),
    ("In which country were French Fries originally invented?", "Your answer ", options_14, "B"),
    ("What iconic video game character was originally named 'Jumpman' in 1981?", "Your answer ", options_15, "C")
          ]
    random.shuffle(questions)
    return questions

def pop_quiz_game():
    m=0
    questions= random_questions()
    for num in range(5):
        question, prompt, options, correct_answer = questions[num]
            
        print(f"Question {num + 1}")
        answer= pop_quiz(question, prompt, options, correct_answer)
        m=points(m, answer, correct_answer)
    print(f"Your total score is {m}/5")
    return m
    
    
def points(m, answer, correct_answer):
    if answer==correct_answer:
        m=m+1
    else:
        m=m+0
    return m









users = {             #Användarnamn resp lösen (Fler användare kan läggas till)
    "Fei": "100",
    "Mollie": "1367",
    "Bosse": "ko"
}
while True:   
    login_splash()
    user_name = login(users) 

    if user_name is None: #om svaret är quit när man skrivit in sina uppgifter så skriver den Goodbye!
        print("Goodbye!")
        print()
        break #programmet avslutas helt!

    result = main_menu(user_name) #menyn där du väljer mellan spelen eller log out

    if result == "logout":
        print()
        print("You have been logged out.") #därefter börjar login (while)loopen igen, vilket gör det möjligt för ny användare att logga in
        print()

        
