def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are equal
    if len(str1) != len(str2):
        return False

    # Count occurrences of each character in both strings
    char_count = {}

    # Increment count for characters in the first string
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement count for characters in the second string
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  # Character not present in first string

    # Check if all character counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True

# Test the function
string1 = "hii"
string2 = "smile"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
