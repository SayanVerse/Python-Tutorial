class calculator:
    def __init__(self, a):
        self.a=a
    
    def square(self):
        print(f"THE SQUARE OF {self.a} IS {self.a*self.a}")
    def cube(self):
        print(f"THE cube OF {self.a} IS {self.a*self.a*self.a}")
    def sqroot(self):
        print(f"The square root of {self.a} is {self.a**1/2}")
    
    @staticmethod
    def greet():
        print("Good Morning!\n")
        
            
x=calculator(16)
x.greet()
x.square()
x.cube()
x.sqroot()
