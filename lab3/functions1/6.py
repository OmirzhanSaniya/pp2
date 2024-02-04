def reverse(input_str):
    words = input_str.split() 
    reversed_words = words[::-1] 
    reversed_str = ' '.join(reversed_words)  
    return reversed_str

s = reverse(input())
print(s)