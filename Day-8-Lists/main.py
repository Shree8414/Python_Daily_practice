# Day 8: Lists in Python

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
print("After adding:", numbers)

numbers.remove(30)
print("After removing:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print("Sum:", sum(numbers))

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Even numbers count:", even_count)

numbers.reverse()
print("Reversed list:", numbers)