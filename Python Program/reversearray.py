def custom_sort_and_reverse(arr):
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
    
    # Reverse the entire array
    sorted_arr.reverse()
    
    return sorted_arr

# Example 
arr = [5,3,2,1,8]
sorted_and_reversed_arr = custom_sort_and_reverse(arr)
print("Original Array:", arr)
print("Sorted and Reversed Array with first half in ascending and second half in descending:", sorted_and_reversed_arr)
