def count_vowels_and_consonants(input_string):
    # Convert the input string to lowercase to ensure case insensitivity
    input_string = input_string.lower()

    # Initialize counters for vowels and consonants
    num_vowels = 0
    num_consonants = 0

    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Iterate over each character in the string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Increment the respective counter based on whether it's a vowel or consonant
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

# Test the function
input_string = "Hello World"
vowels, consonants = count_vowels_and_consonants(input_string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
