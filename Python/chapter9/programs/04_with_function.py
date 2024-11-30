'''
f=open("sayan.txt")
data=f.read()
print(data)
f.close()

the same can be written like this
'''
with open("sayan.txt") as f:
    print(f.read())
    