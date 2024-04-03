def count_even_and_odd(arr):
    even_count = 0
    odd_count = 0
    
    # Iterate through the elements of the array
    for num in arr:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
        else:
            odd_count += 1  # If not even, it's odd
    
    return even_count, odd_count

# Example 
arr = [1, 2, 3, 4, 5]
even_count, odd_count = count_even_and_odd(arr)
print("Number of even integers:", even_count)
print("Number of odd integers:", odd_count)
