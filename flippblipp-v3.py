def flippblipp_game():


    def flippblipp(m):
        if m % 3 == 0 and m % 5 == 0:
            return("flipp blipp")
            
        elif m % 3 == 0:
            return("flipp")
            
        elif m % 5 == 0:
            return("blipp")
        
        else:
            return(m)

    n = 1

    play = True

    print("	", 1)

    while play:
        n = n + 1
        
        answer = input("Nästa:	 ")
        correct_answer = flippblipp(n)
        
        if answer == str(correct_answer): #jämförs spelarens svar.
            pass
        # pass, gör inget om svaret är rätt. 
            
        else:
            print("Fel -", correct_answer)
            print()
            print("Game over")
            play = False
        
        
        