# Function to find symmetric difference
def find_symmetric_difference(set1, set2):
    # Using symmetric_difference() method
    return set1.symmetric_difference(set2)

# Example A
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}
sym_diff_a = find_symmetric_difference(set1_a, set2_a)
print(f"Symmetric difference of Set1 and Set2 (Example A): {sym_diff_a}")

# Example B
set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}
sym_diff_b = find_symmetric_difference(set1_b, set2_b)
print(f"Symmetric difference of Set1 and Set2 (Example B): {sym_diff_b}")
