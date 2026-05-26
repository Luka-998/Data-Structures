# Leetcode Arrays 

# 14. Longest commong prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

strs = ["flower","flow","flight"]

def get_prefix(arr):
    
    # rearrange array

    min_len = arr[0]
    for name in arr:
        if len(name) < len(min_len):
            min_len = name
    
    i = 0
    while i < len(min_len): # flow
        for s in arr:
            if s[i] != arr[0][i]: #f
                return s[:i]

        i+=1
    return strs[0][:i]

z = get_prefix(strs)
print(z)

