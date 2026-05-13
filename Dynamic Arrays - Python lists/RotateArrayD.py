# Rotate an Array by d - Counterclockwise or Left

"""
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}

"""

arr = [1, 2, 3, 4, 5, 6]
arr2 = [1,2,3]
d = 2
d2 = 4

def rotate_array(arr):

    for i in range(d2):
        left = arr.pop(0)
        arr.append(left)  
    return arr

z = rotate_array(arr2)
print(z)