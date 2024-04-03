def find_indices_with_sum(arr, target):
    complements = {}  # Dictionary to store complements and their corresponding indices

    for i, num in enumerate(arr):
        complement = target - num
        if complement in complements:
            return complements[complement], i
        complements[num] = i

    return None  # If no such pair is found

# Test the function
arr = [2, 7, 11, 15]
target = 9
indices = find_indices_with_sum(arr, target)
if indices:
    print(f"Indices of elements with sum {target}: {indices}")
else:
    print("No such pair found.")
