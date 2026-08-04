"""
 Find First and Last Position of Element in Sorted Array

 Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
nums = [5,7,7,8,8,10] # 2
target  = 8


# output [3,4]

<<<<<<< HEAD
def solution(nums,target,leftBias):
    left = 0
    right = len(nums) - 1
    candidate = -2
=======
def solution(nums,target):

    left = 0
    right = len(nums) - 1
    found = []
>>>>>>> f40d8ac025847d8500919bdb70039e1b6210c01d
    
    # basecase
    
    if nums == []:
        return [-1,-1]

    while left <= right:
        middle = (left+right) // 2
<<<<<<< HEAD
        
=======
        print(middle)
>>>>>>> f40d8ac025847d8500919bdb70039e1b6210c01d

        if target < nums[middle]:
            right = middle -1 
        elif target > nums[middle]:
            left = middle +1
        elif target == nums[middle]:
<<<<<<< HEAD
            candidate = middle
            # left
            if leftBias:
                right = middle - 1  
            else:
                left = middle + 1
    return candidate
=======
            found.append(middle)
            right = middle - 1

    return found
>>>>>>> f40d8ac025847d8500919bdb70039e1b6210c01d
    





<<<<<<< HEAD
z1 = solution(nums,target,leftBias=True)
z2 = solution(nums,target,leftBias=False)
res = [z1,z2]
print(res)
=======
z = solution(nums,target)
print(z)
>>>>>>> f40d8ac025847d8500919bdb70039e1b6210c01d
