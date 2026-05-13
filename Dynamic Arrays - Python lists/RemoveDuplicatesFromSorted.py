# Remove duplicates from Sorted Array

"""
Given a sorted array arr[] of size n, 
the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. 
Additionally, return the length of this distinct sorted subarray.

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: All the elements are 2, So only keep one instance of 2.

space O(1) solution

"""

array = [2, 2, 2, 2, 3, 4]

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    
    write_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[write_index - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index

z = remove_duplicates(array)
print(z)
print(array[:z])