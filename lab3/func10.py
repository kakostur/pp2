def unique_elements(input_list):
    unique_list = []
    
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    
    return unique_list

input_list = [1, 2, 3, 3, 4, 4, 5]
result = unique_elements(input_list)
print("List with unique elements:", result)
