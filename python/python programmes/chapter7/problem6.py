#write a programme to find the factorial  of a natural number using
# using while loop
n=int(input("Enter the number:"))
i=1
fac=1
if(n==0):
    print(f"The factorial  is : 0")
else:
    
    while(i<=n):
        fac=fac*i
        i=i+1
    print(f"The factorial is :{fac}")