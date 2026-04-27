text1 = 'radar'
text2 = 'level'
text3 = 'python'

def check_palindrome(x):

    # Base case
    # String is 1 character -> True

    if len(x)<=1:
        return True
    
    if x[0] != x[-1]:
        return False
    
    return check_palindrome(x[1:-1])

result = check_palindrome(text2)

print(result)
    