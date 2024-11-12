#write a python program to print the sum of n number using recursion
#formula = n(n+1)/2
def sum_of_n(n):
    sum=0
    for i in range (1,n+1):
        sum=sum+i
    return(f"the sum of {n} natural number is : {sum}")

#method 2:
def sum_of_n_method2(x):
    s=((x*(x+1))/2)
    return(f"the sum of {x} natural number is : {s}")
    
    
    
    
    
    
a=int(input("Enter the number:"))
print(sum_of_n_method2(a))
        
         