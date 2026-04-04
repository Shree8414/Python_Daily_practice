# Day 7: Functions in Python

# 1. Sum of two numbers
def add(a, b):
    return a + b


# 2. Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 3. Prime number check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 4. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# ----------- MAIN PROGRAM -----------

print("Sum:", add(5, 3))
print("Even/Odd:", check_even_odd(7))
print("Is Prime:", is_prime(7))
print("Factorial:", factorial(5))