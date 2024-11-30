num = int(input("Enter the number: "))

if num <= 1:
    print(f"{num} is not a prime number!")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number!")
            break
    else:
        # This else aligns with the for loop and only executes if no break occurs
        print(f"{num} is a prime number!")
