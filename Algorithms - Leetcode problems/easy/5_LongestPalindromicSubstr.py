# 5. Longest Palindromic Substring

# Given a string s return a longest palindromic substring.
"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""

s = "abcda"

def get_palindrome(arr):

    total_len = 0
    res = []
    curr = ''

    if arr == '':
        return False
    
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return arr[0]
        
    max_len = 0
    max_curr = arr[0]

    for i in range(len(arr)):
        curr = ""
        for j in range(i,len(arr)):
            curr+=arr[j]
            if len(curr) > 2:
                if curr == curr[::-1] and len(curr) > max_len:
                    max_len = len(curr)
                    max_curr = curr
    return max_curr
                    
    
d = get_palindrome(s)
print(d)