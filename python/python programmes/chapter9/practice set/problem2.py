'''
the game() function ia a program lets user play a game and returns a score in int.
you need to read a file "high_score.txt" which is either blank or
 contains previous higscore .
 wap to read the highscore whenever the game function breaks the highscore!
'''
import random
def game():
    print("You are playing the game ..")
    score= random.randint(1,62)
    
    
    #fetch the highscore
    with open ("highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore= 0
            
            
    print(f"Your score is : {score}")
    
    
    
    if (score>highscore):
        #write this highscore to this file
        with open("highscore.txt" , "w") as f:
            f.write(str(score))
    return score

game()


