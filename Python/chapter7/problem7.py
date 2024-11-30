'''
      *
    * * *
  * * * * * using loop
'''
n = int(input("Enter the value: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")        # Adjust spaces to center the pyramid
    print("* " * ((2 * i) - 1))         # Use odd number of asterisks to match the pattern
