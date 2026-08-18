"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""


target = 1
nums = [1,4,4]

def solution(nums,target):

    res = len(nums) + 1
    window_sum = 0

    left = 0
    right = 0
    
    while right < len(nums):
        window_sum+=nums[right]
        while window_sum >= target:
            res = min(right - left + 1, res)
            window_sum -=nums[left]
            left+=1
        right+=1


    if res == len(nums) + 1:
        return 0
    else:
        return res


z = solution(nums,target)
print(z)