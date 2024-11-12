#create a CLASS fro progarmmer storing information of few programmer working at microsoft
class Programmer:
    company="Microsoft"
    
    def __init__(self, name, code, salary):
        self.name=name
        self.code=code
        self.salary=salary
        
    @staticmethod
    def greet():
        print("Good morning")
                


a=Programmer("Sayan",12,200000)
a.greet()
print(a.name, a.code, a.salary)

b=Programmer("Sourik", 13, 100000)
print(b.name, b.code, b.salary)

