def rotate_left(arr):
    if len(arr) <= 1:
        return arr  # No need to rotate if array has 0 or 1 element

    first_element = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]  # Shift each element one position to the left
    arr[-1] = first_element  # Move the first element to the end
    return arr

# Test the function
arr = [9,1,7,5,2]
rotated_arr = rotate_left(arr)
print("Original array:", arr)
print("Array rotated left by 1 position:", rotated_arr)
