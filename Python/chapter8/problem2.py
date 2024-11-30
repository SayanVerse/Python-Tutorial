#Write a python function to convert Celsius to Fahrenheit
def c_to_f(c):
    far=((9/5)*c)+32
    return far
    #return(f"{c} degree Celcius = {far} farenhite")

a=int(input("Enter the temperature in c:"))
print(f"{a} degree celcius = {c_to_f(a)} farenhite")