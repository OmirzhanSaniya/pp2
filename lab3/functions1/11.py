def is_palindrome(str):
    if str == str[::-1]:
        return True
    return False    

print(is_palindrome(str(input().lower().replace(" ", ""))))