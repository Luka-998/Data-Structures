# 395 -  Longest Substring with At Least K Repeating Characters


"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

"""

s = "ababacb"
target = 3

def solution(arr,target):

    res = 0

    for i in range(len(arr)):
        current = ''
        tracker = {}
        for j in range(i,len(arr)):
            current +=arr[j] # a , b {a:1, b:1}
            print(current)
            if arr[j] not in tracker:
                tracker[arr[j]] = 1
            else:
                tracker[arr[j]] +=1
            for key,value in tracker.items():
                if not value >= target:
                    pass
                elif len(current) > res:
                    res = len(current)

                
    if res == 0:
        return 0
    else:
        return res
        

z = solution(s,target)
print(z)
        


