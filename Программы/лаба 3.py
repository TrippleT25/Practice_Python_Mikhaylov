def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

input_list = [[1, 6, 3], [4, 8], [2, 7, 5, 9]]

flattened_list = flatten_list(input_list)

print("Исходный список списков:", input_list)
print("Плоский список:", flattened_list)
