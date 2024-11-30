'''Write a programme to find your name is present in the list'''

names=["sayan","sourab"]
username=input("Enter your name:").lower()
if username in names:
    print("your name is present in list!\n")
else:
    print("your name is not present in list!\n")
    