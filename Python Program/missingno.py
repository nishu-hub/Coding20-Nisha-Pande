def find_missing_number(arr):
    n = len(arr) + 1  # Expected length of the array including the missing number
    total_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    
    # Calculate the sum of elements in the array
    array_sum = sum(arr)
    
    # The difference between the total sum and the sum of elements in the array will be the missing number
    missing_number = total_sum - array_sum
    
    return missing_number

# Example 
arr = [ 0,1,2, 5, 6]
missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)
