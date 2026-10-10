"""
238. Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"BRUTE FORCE"

nums = [1,2,3,4]

def solution(array):
    """
        for loop goes over each position in the nums array
        inner loop: from start , skipping current index , *= others
    
    """ 
    result = [1] * len(array)

    for i in range(len(array)):
        current = 1
        for j in range(len(array)):
            if j != i:
                current*=array[j]
        result[i] = current
    return result

z = solution(nums)

# Brute force fine

def solution_o_n(array):
    
    """
        One for loop, prefixPrd calculates left product 
        suffixProd calculates right product 
        both excluding current index


    - error encountered -> Cant index slice of the list pre & post index ?
    - How to solve this?
    
    """
    leftProd = 1
    rightProd = 1
    result = [1] * len(array)

    for r in range(len(array)):
        result[r] = leftProd
        leftProd*=array[r]
    rightProd=1
    for i in range(len(array))[::-1]:
        result[i] *= rightProd
        rightProd *=array[i]
    return result
    
z = solution_o_n(nums)
print(z)