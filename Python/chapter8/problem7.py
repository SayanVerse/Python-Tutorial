#print multiplication table using function
def multiplication_table(n):
    if(n==0):
        print("0")
    else:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
            


a=int(input("Enter the value:"))
multiplication_table(a)