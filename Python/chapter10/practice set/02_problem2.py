#Write a class “Calculator” capable of finding square, cube and square root of a
#number.
import math

class calculator:
    def __init__(self, a):
        self.a=a
        
    def square(self):
        print(f"the square is {self.a*self.a}")
        
    def cube(self):
        print(f"The cube is {self.a*self.a*self.a}")
        
    def squareroot(self):
        print(f"the square root is : {math.sqrt(self.a)}")
        
        
a=calculator(16)
a.cube()
a.square()
a.squareroot()