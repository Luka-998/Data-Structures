# Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


"""

s = "pwwkew"

def get_longest(s):

    max_count = 0

    for i in range(len(s)):
        
        current_count = 0
        current_sub = ''
        for j in range(i,len(s)):
            if s[j] not in current_sub:
                
                current_sub+=s[j]
                current_count+=1
                if current_count > max_count:
                    max_count= current_count
            else:
                
                if current_count > max_count:
                    max_count = current_count
                break
    return max_count

p = get_longest(s)
print(p)