def tuple_average(tup):
    if len(tup) == 0:
        return 0  # Return 0 if the tuple is empty to avoid division by zero
    return sum(tup) / len(tup)

# Example usage:
my_tuple = (10, 20, 30, 40)
average = tuple_average(my_tuple)
print(f"The average of the tuple is: {average}")
