def sort_selection(list_data):
    length = len(list_data)
    for start in range(length - 1):
        lowest = start
        for check in range(start + 1, length):
            if list_data[check] < list_data[lowest]:
                lowest = check
        # swap using a temp variable
        temp = list_data[start]
        list_data[start] = list_data[lowest]
        list_data[lowest] = temp
    return list_data

# Test cases
print(sort_selection([1, 2, 3]))       # [1, 2, 3]
print(sort_selection([3, 2, 1]))       # [1, 2, 3]
print(sort_selection([29, 10, 14, 37, 14]))  # [10, 14, 14, 29, 37]
