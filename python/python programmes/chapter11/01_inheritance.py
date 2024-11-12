class employee:
    company="ITC"
    name="sayan"
    def show(self):
        print(f"The name of the enmployee is : {self.name} and the salary is {self.salary}")
        
class programmer(employee):
    company="ITC infotech"
    def showlanguage(self):
        print(f"The name of the employee is {self.name} and {self.name} is good with {self.language}")
        
a=programmer()
b=employee()
print(a.company, b.company, a.name, b.name)
