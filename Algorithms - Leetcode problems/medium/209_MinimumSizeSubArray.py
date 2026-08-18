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

target = 15
nums = [1,2,3,4,5]

def solution(nums,target):

    res = len(nums) + 1

    for i in range(len(nums)):
        current = 0
        for j in range(i,len(nums)):
            current+=nums[j]
            if current >= target:
                print(nums[i:j+1])
                if len(nums[i:j+1])<res: 
                    res = len(nums[i:j+1])
                elif len(nums[i:j+1])==res:
                    res = len(nums[i:j+1])
    if res == len(nums) + 1:
        return 0
    else:
        return res

p = solution(nums,target)
print(p)

# Test case is not passed because problem solution requires O(n) time, and this approach is O(n^2)
# brute force solved


# O(n) time complexity solution, sliding window (expected approach)
nums2 = [2,3,1,2,4,3]
target2 = 7 

def solution_sliding(nums,target):
    res = len(nums) + 1
    left = 0
    window_sum = 0
    for right in range(len(nums)):
        window_sum +=nums[right]
        while window_sum >= target:
            res = min(right-left+1,res)
            window_sum -=nums[left]
            left+=1

    if res == len(nums) + 1:
        return 0
    else:
        return res

            


z = solution_sliding(nums2,target2)
print(f"Solution: {z}")