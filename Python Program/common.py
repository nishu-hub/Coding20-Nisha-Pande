def find_common_elements(arr1, arr2):
    common_elements = []
    
    # Iterate through the elements of the first array
    for elem in arr1:
        # Check if the element exists in the second array and is not already in the common_elements list
        if elem in arr2 and elem not in common_elements:
            common_elements.append(elem)
    
    return common_elements

# Example 
arr1 = [1, 2, 3,5]
arr2 = [3, 4, 6, 7]
common_elements = find_common_elements(arr1, arr2)
print("Common elements between the two arrays:", common_elements)
