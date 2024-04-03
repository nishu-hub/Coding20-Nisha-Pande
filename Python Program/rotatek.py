def rotate_left(arr, k):
    if len(arr) <= 1 or k % len(arr) == 0:
        return arr  # No need to rotate if array has 0 or 1 element or if k is multiple of array length

    k = k % len(arr)  # Ensure k is within the range of array length

    # Rotate the array k times
    for _ in range(k):
        first_element = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
        arr[-1] = first_element

    return arr

# Test the function
arr = [7,0,8,2,8,5,9]
k = 2  # Number of positions to rotate left
rotated_arr = rotate_left(arr, k)
print("Original array:", arr)
print(f"Array rotated left by {k} positions:", rotated_arr)
