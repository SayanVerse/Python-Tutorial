''' A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams'''
a="make a lot of money"
b="buy now"
c="subscribe this"
d="click this"
user_comment=input("Enter the comment:")
if(a.lower() in user_comment or b.lower() in user_comment or c.lower() in user_comment or d.lower() in user_comment):
    print(f"The comment '{user_comment}' is spam!")
else:
    print(f"The comment '{user_comment}' is not spam!")
    
    
