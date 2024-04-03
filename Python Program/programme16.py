def is_pangram(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Create a set to store unique letters
    letters_seen = set()

    # Iterate over each character in the string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            letters_seen.add(char)

    # Check if all 26 letters of the alphabet are present
    return len(letters_seen) == 26

# Test the function
input_string = "Hey,My name is Pankaj"
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
