'''
stone - paper -scissor game
-1 for stone
0 for paper
1 for scissor
'''
import random                 #import random number generator
pc=random.choice([-1,0,1])

dic={
    "s":-1,"p":0,"sc":1
}

rev_dic={
    -1:"s",0:"p",1:"sc"
}

user_input=input("Enter your choice:")
user=dic[user_input.lower()]   #.lower() to convert all in lower

print(f"Your choice is :{user_input}\nComputer choice is :{rev_dic[pc]}\n")
if(pc==user):
    print("Opps! Its a draw!")
else:
    if(user==0 and pc==1):
        print("Opps! You lose the game!")
    elif(user==0 and pc==-1):
        print("Hurrah! You win the game!")
    elif(user==1 and pc==0):
        print("Hurrah! You win the game!")
    elif(user==1 and pc==-1):
        print("Opps! You lose the game!") 
    elif(user==-1 and pc==1):
        print("Hurrah! You won the game!") 
    elif(user==-1 and pc==0):
        print("Opps! You lose the game!") 