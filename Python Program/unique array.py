def print_unique_numbers(arr):
    unique_numbers = set()  # Initialize an empty set to store unique numbers
    
    for num in arr:
        if arr.count(num) == 1:  # Check if the number occurs only once in the array
            unique_numbers.add(num)  # Add the unique number to the set
    
    # Print the unique numbers
    print("Unique numbers in the array:", unique_numbers)

# Example 
arr = [1, 2, 3, 4, 5, 2, 3,5]
print_unique_numbers(arr)
