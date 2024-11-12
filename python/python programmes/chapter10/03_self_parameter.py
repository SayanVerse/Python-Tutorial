class employee:
    language ="python"
    salary=1200000
    
    def getinfo(self):
        print(f"The language is {self.language}.\nThe salary is {self.salary}")
        
    def greet(self):
        print("Good Morning!")
        





sayan=employee()
sayan.language = "HTML-CSS"
sayan.greet()

employee.getinfo(sayan)    #sayan.getinfo()  these 2 are same 


