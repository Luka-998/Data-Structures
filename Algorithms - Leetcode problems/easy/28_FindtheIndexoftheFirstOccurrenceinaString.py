"""

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.


"""

haystack = "sadbutsad" 
needle = "sad"

# first pointer is fixed while second pointer iterate in the length of target word
# i must check every substring of the string , and return first occurence of target word
# to iterate over each substring of string, i must do: string - len(target) + 1

t1 = 'hello'
t2 = 'll'
def get_needle(arr,target):
    
    n = len(target)

    if target not in arr:
        return -1
    else:

        for sub in range(len(arr)-n+1):
            if arr[sub:sub+n] == target:
                return sub


z = get_needle(t1,t2)
print(z)

"working!"