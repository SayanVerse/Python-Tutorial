#write a function to find the greatest of three numbers
def grateset(a,b,c):
    if(a==b and b==c and c==a):
        return(f"{a},{b},{c} all are equal!")
    elif(a>b and a>c):
        return(f"{a} is the gratest number!")
    elif(b>a and b>c):
        return(f"{b} is the gratest number!")
    elif(c>a and c>b):
        return(f"{c} is the gratest number!")
    else:
        return("Somethimg wemt wrong!")      
    
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
print(grateset(a,b,c))
