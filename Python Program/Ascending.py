def custom_sort(arr):
    # Calculate the midpoint of the array
    mid = len(arr) // 2
    
    # Split the array into two halves
    first_half = arr[:mid]
    second_half = arr[mid:]
    
    # Sort the first half in ascending order
    first_half.sort()
    
    # Sort the second half in descending order
    second_half.sort(reverse=True)
    
    # Merge the two sorted halves
    sorted_arr = first_half + second_half
    
    return sorted_arr

# Example 
arr = [9,6,0,8,4]
sorted_arr = custom_sort(arr)
print("Original Array:", arr)
print("Sorted Array with first half in ascending and second half in descending:", sorted_arr)
