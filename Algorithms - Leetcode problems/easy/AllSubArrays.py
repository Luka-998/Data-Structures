# Generating All Subarrays
# Given an array arr[], the task is to generate all the possible subarrays of the given array.

"""
Input: arr[] = [1, 2, 3]
Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]
"""

array = [1, 2, 3]

def get_all(arr):
    
    result = []

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
            
            
    return result
z = get_all(array)
print(z)