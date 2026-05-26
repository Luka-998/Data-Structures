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
    
        min_len = strs[0]
        for name in strs:
            if len(name) < len(min_len):
                min_len = name
    
        i = 0
        while i < len(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        return strs[0][:i]
"""
finish this

"""

        
            

            

z = get_prefix(strs)
print(z)
"""
u prvom delu dodat je prvi indeks prve reci 'f' u total curr
> izlazim iz prve reci 

ulazim u 'flow'
prefix je i dalje 0 

nije empty:
moram da upored prvi string iz total_curr sa prvim indeksom druge i trece reci
ako su isti total_curr ostaje 
"""