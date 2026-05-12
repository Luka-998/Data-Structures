# Remove duplicates from Sorted Array

"""
Given a sorted array arr[] of size n, 
the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. 
Additionally, return the length of this distinct sorted subarray.

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: All the elements are 2, So only keep one instance of 2.

space O(n) solution first

"""

array =  [2, 2, 2, 2]

def remove_duplicates(arr):
    #base case

    seen = False
    new_list = []
    for i in range(len(arr)):
        if arr[i] not in new_list and arr[i] is not seen:
            new_list.append(arr[i])
            seen = True
    return new_list

z = remove_duplicates(array)
print(z)