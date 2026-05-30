# 35. Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

nums = [1,3,5,6]
target = 7
def return_target(arr,target):
    left = 0
    right = len(nums) - 1

    

    while left < right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    return left
    
z = return_target(nums,target)
print(z)


# time O(nlog) -> binary serachs halfs the feature space in each iteration, leading to a much
# efficient way than using for loop O(n) time.