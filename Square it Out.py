def square_and_filter(begin, end):
    # Generate a list of square values within the specified range
    square_values = [num**2 for num in range(begin, end + 1)]

    # Separate the squares into odd and even values
    even_squares = [val for val in square_values if val % 2 == 0]
    odd_squares = [val for val in square_values if val % 2 != 0]

    # Print the results
    print(f"Square values: {square_values}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

# Example usage:
begin = 1
end = 10
square_and_filter(begin, end)
