from itertools import islice

def chunks(lst, chunk_size):
    it = iter(lst)
    while chunk := list(islice(it, chunk_size)):
        yield chunk

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(chunks(my_list, 3))
print(result)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]
