import re

def remove_non_alphabetic(input_string):
    # Use regular expression to remove all non-alphabetic characters
    return re.sub(r'[^a-zA-Z]', '', input_string)

# Test the function
input_string = "Hello906, World!"
result = remove_non_alphabetic(input_string)
print(result)  
