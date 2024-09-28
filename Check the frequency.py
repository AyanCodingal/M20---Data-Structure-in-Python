# Given test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter the value for which they want to check the frequency
value_to_check = int(input("Enter the value to check its frequency: "))

# Check the frequency of the value in the dictionary
frequency = list(test_dict.values()).count(value_to_check)

# Print the frequency of the value
print(f"The frequency of value {value_to_check} in the dictionary is: {frequency}")
