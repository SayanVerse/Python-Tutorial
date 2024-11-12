'''A username is approved when it contains ten characters. 
Write a programme to cheque if the username has 10 charecter'''


username=input("Enter your name :")
if(len(username)>=10):
    print(f"username:{username} is approved!")
else:
    print(f"username:{username} is not approved!")
    