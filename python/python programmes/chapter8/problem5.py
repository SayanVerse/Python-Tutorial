#inch_to_cm
def inch_to_cm(inch):
    cm=inch*2.54
    return(f"{inch} inch = {cm} cm")




a=float(input("Enter the value in inch:"))
print(inch_to_cm(a))