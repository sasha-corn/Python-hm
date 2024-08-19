import string


def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char not in string.punctuation and char != ' ')
    text2 = text[::-1]
    return True if text == text2 else False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
