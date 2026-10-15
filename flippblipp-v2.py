
def flippblipp(m):
    if m % 3 == 0 and m % 5 == 0:
        return("flipp blipp")
        
    elif m % 3 == 0:
        return("flipp")
        
    elif m % 5 == 0:
        return("blipp")
    
    else:
        return(m)

n = 10

for m in range(1, n+1):
    print(flippblipp(m))
    

