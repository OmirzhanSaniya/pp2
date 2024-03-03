def is_palindrome(s):
    return list(s) == list(reversed(s))

str = input()

if is_palindrome(str):
    print("Yes")
else:
    print("No")