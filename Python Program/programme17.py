def is_armstrong_number(num):
    # Convert the number to a string to determine its length
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Test the function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
