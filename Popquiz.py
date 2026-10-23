import random
import time 

def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("		Pop Quiz")
    print()
    print("      Test your all-around knowledge "   )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
splash()

    
        

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

def run_quiz():
    n=0
    questions= random_questions()
    for num in range(5):
        question, prompt, options, correct_answer = questions[num]
            
        print(f"Question {num + 1}")
        answer= pop_quiz(question, prompt, options, correct_answer)
        n=points(n, answer, correct_answer)
    print(f"Your total score is {n}/5")
    
    
def points(n, answer, correct_answer):
    if answer==correct_answer:
        n=n+1
    else:
        n=n+0
    return n
    

run_quiz()

