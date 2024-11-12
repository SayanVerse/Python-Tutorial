from random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    
    
    def book(self, source, destination):
        print(f"your ticket is booked successfully in train no {self.trainNo} from {source} to {destination}!")
    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time !")
    def getFare(self, source, destination):
        print(f"The ticket fare for train no : {self.trainNo} from {source} to {destination} is {randint(999,4999)}")
        
        
user=train(12786)
user.book("howrah", "New Delhi")
user.getStatus()
user.getFare("howrah", "New Delhi")