def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test the function
arr = [1,2,5,5,8,9,1]
unique_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Array with duplicates removed:", unique_elements)
