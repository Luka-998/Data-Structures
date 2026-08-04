# 209. Minimum Size Subarray Sum
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

target = 7
nums = [2,3,1,2,4,3]

def solution(nums,target):

    min_len = 0

    for i in range(len(nums)):
        current = 0
        for j in range(len(nums)):
            current+=nums[j]
            current_len = len(nums[i:j+1])
            if current >= target:
                if current_len < min_len:
                    min_len = current_len
    return min_len
            


               
p = solution(nums,target)
print(p)

