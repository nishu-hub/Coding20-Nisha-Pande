def is_palindrome(n):
    return str(n) == str(n)[::-1]

number = input("Enter a number: ")
if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a palindrome")
