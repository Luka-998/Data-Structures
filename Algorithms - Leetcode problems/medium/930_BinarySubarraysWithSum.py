"""
930. Binary Subarrays With Sum
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""
nums = [1,0,1,0,1] 
goal = 2

# arrays with sum <= 2 (0,1,2)
# arrays with sum <=1 (0,1)

def at_most(arr,at_most_num):
    res = 0
    left= 0
    curr =0
    for r in  range(len(arr)):
        curr+=arr[r]
        while curr > at_most_num:
            curr -=arr[left]
            left+=1

        res +=1
    return res



z = at_most(nums,2)
print(z)
"""
def solution(arr,goal):
    at_most_2 = 0
    while at_most_2 <= goal:

    res = 0


z = solution(nums,goal)
print(z)
"""