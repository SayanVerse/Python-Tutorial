class employee:
    language = "Python"
    salary = 120000
   #this is a class attribute 
    
emp_1= employee()
emp_1.name = "Sayan"  #this is an instance atttibute


emp_2=employee()
emp_2.name="\nRohan"      # this is an instance attribute

print(emp_1.name, emp_1.language,emp_1.salary)

print(emp_2.name, emp_2.language,emp_2.salary)

#here name is an instance attribute and language,salary  is an object attribute , they are directly belong to clASS