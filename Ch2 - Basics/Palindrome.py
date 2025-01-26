word = input ("Test if a word in a palindrome:")


def is_palindrome(word):
    word = word.replace(" "," ").lower()
    if word == word [::-1]:
         return True
    else:
         return False

print (is_palindrome(word))