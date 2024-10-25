def merge_dicts(dict1, dict2):
    result = {} 

    for key, value in dict1.items():
        result[key] = value

    for key, value in dict2.items():
        if key in result:
            result[key] += value 
        else:
            result[key] = value  

    return result

dict1 = {'a': 200, 'b': 50}
dict2 = {'a': 100, 'c': 500}

merged = merge_dicts(dict1, dict2)
print(merged)
