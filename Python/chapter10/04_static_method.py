class employee:
    language ="python"
    salary=1200000
    
    def getinfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
     
    @staticmethod   
    def greet():
        print("Good Morning!")
        
'''Static method is a method, we use this method in that function,
where object(self) is not needed.
like this, good morning function does not require any object.
so we can pass here static metjod @staticmethod to greet good morning without any obj ;'''

sayan=employee()
sayan.language = "HTML-CSS"

employee.getinfo(sayan)    #sayan.getinfo()  these 2 are same 

sayan.greet()

