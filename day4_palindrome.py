# Day 4 Program: Palindrome Check (String)

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")