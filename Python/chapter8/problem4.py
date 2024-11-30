'''
*****
****
***
**
*
print this patten by python function
'''
def pattern(a):
    if(a==0):
        return None
    else:
        print("*\n"*a)
        pattern(a-1)


x=int(input("Enter the value:"))        
print(pattern(x))