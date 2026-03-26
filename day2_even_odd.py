# Day 2 Program: Check Even or Odd

num = int(input("Enter a number: "))

if num == 0:
    print("0 is neither even nor odd")
elif num % 2 == 0:
    print("Even number")
else:
    print("Odd number")