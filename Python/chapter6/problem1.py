a=int(input("Enter the first number:" ))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
d=int(input("Enter the fourth number:"))
if(a==b & b==c & c==d & d==a):
    print(f"{a} , {b} , {c} & {d} all numbers are equal!")
elif(a>b & a>c & a>d):
    print(f"{a} is the gratest number!")
elif(b>a & b> c & b>d):
    print(f"{b} is the gratest number !")
elif(c>a & c>b & c>d):
    print(f"{c} is the gratest number !")
elif(d>a & d>b & d>c):
    print(f"{d} is the gratest number!")
else:
    print("something went wrong!")