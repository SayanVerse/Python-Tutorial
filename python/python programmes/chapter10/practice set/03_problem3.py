class demo:
    x=4
    
a=demo()
print(a.x)   #print the class attribute because instance attribute is not present
a.x=10       #instance attribute isn set
print(a.x)   #print the instance attribute
print(demo.x)    #print the class attributes