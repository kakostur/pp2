def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

input_word = input()
if is_palindrome(input_word):
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
