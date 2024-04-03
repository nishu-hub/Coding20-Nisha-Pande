def word_with_highest_repeated_letters(input_string):
    words = input_string.split()
    max_word = ""
    max_repeated_letters = -1

    for word in words:
        letter_count = {}
        for letter in word:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1

        if letter_count:
            max_repeat = max(letter_count.values(), default=0)
            if max_repeat > 1 and max_repeat > max_repeated_letters:
                max_word = word
                max_repeated_letters = max_repeat

    if max_word:
        return max_word
    else:
        return -1

# Example:
input_string_1 = "abcdefghij google microsoft"
input_string_2 = "cameron blue"
print(word_with_highest_repeated_letters(input_string_1))
print(word_with_highest_repeated_letters(input_string_2))
