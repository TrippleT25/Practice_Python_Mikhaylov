import json

def convert_to_json_if_integer_lists(input_dict):
    filtered_dict = {
        key: value for key, value in input_dict.items()
        if isinstance(value, list) and all(isinstance(item, int) for item in value)
    }
    
    return json.dumps(filtered_dict)

example_dict = {
    "a": [1, 2, 3],
    "b": [1.5, 2.5, 3.5],
    "c": ["string", "another string"],
    "d": [4, 5, 6],
    "e": [7, "eight", 9]
}

result = convert_to_json_if_integer_lists(example_dict)
print(result)  # Вывод: {"a": [1, 2, 3], "d": [4, 5, 6]}
