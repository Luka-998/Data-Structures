# 1. Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


-------

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
nums = [3,2,4]
target = 6

def solution(arr,target):
    
    seen_numbers = {}

    """
    Intuition: 

    1) For each number, target - current number is complement, and if that complement exists
    in the hashmap, that means we have a solution [currentNumber_index,seen_number[complement]]
    
    """

    for i in range(len(arr)):

        complement = target - arr[i]
    
        if complement in seen_numbers: # on 3rd iteration, this is true
            print(seen_numbers)
            return [seen_numbers[complement],i]

        seen_numbers[arr[i]] = i

    
    
    
z = solution(nums,target)
print(z)

