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


