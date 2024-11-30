class employee:
    language ="python"
    salary=1200000
    
    
    def __init__(self, name, language, salary):
        self.name=name
        self.language=language
        self.salary=salary
        print("I am creating an object!\n")
        
    def getinfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
     
    @staticmethod   
    def greet():
        print("Good Morning!")
        
        
sayan = employee("sayan", "Javascript", 1209989)
sayan.getinfo()
print(sayan.name, sayan.language, sayan.salary)
