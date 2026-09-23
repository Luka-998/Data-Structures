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

def solution(arr,goal):
    res = 0

    right = 0
    left = 0
    while left < len(arr):
        current = sum(arr[left:right])
        if current != goal:
            right+=1

        else:
            res+=1
            left+=1
            right=left
    return res


z = solution(nums,goal)
print(z)