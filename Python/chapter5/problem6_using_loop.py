d={}
for i in range(1,5):
    name=input(f"Enter name{i}:")
    lan=input("Enter your favourite language:")
    d.update({name : lan})
print(d)