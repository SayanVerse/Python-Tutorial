'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. '''

b=int(input("Enter the marks in bengali:"))
e=int(input("Enter the marks in english:"))
m=int(input("Enter the marks in math :"))

total_marks=(b+e+m)/3

if(total_marks>=40 and b>=33 and e>=33 and m>=33 ):
    print("You have passed in the exam!")
else:
    print("You have failed !")
    