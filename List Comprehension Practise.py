# Take an input number from the user
number = int(input("Enter a number: "))

# List comprehension for odd numbers below the input value and even numbers
odd_numbers = [num for num in range(number) if num % 2 != 0]
even_numbers = [num for num in range(number) if num % 2 == 0]

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Using list comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Display the results
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Capitalized fruits:", capitalized_fruits)
