#write a program to sum a list with 4 numbers.
num=[]

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))
num.append(num1)
num.append(num2)
num.append(num3)
num.append(num4)

num.sort()
print(f"The list of the numbers are : {num}")
#sum=((num[num1])+(num[num2])+(num[num3])+(num[num4]))
print("The sum of numbers in list is :",sum(num))

