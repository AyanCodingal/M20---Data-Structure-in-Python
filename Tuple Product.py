def tuple_product(tup):
    # Initialize product to 1 (multiplicative identity)
    product = 1
    for num in tup:
        product *= num
    return product

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the product of each tuple
print(f"The product of elements in tuple 1 is: {tuple_product(tup1)}")
print(f"The product of elements in tuple 2 is: {tuple_product(tup2)}")
