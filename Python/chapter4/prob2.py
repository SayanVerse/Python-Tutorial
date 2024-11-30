"""Write a program to accept marks of 6 students and display them in a sorted 
manner."""
mark=[]
st1=int(input("Enter your marks:"))
st2=int(input("Enter your marks:"))
st3=int(input("Enter your marks:"))
st4=int(input("Enter your marks:"))
st5=int(input("Enter your marks:"))
st6=int(input("Enter your marks:")) 

mark.append(st1)
mark.append(st2)
mark.append(st3)
mark.append(st4)
mark.append(st5)
mark.append(st6)


mark.sort()
print(mark)




