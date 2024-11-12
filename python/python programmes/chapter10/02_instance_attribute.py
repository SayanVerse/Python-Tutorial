class employee:
    language="python"
    salary = 1200000
    

emp_1=employee()    
emp_1.name="Sayan"
emp_1.language="JavaScript"
print(emp_1.name, emp_1.language)

#Here javascript is  the output instead of python, because of instant attribute Note, instant attribute.
#because instance attribute take preferance over the class attribute 