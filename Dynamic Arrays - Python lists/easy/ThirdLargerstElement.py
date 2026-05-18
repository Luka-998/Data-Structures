"""
Given an array, arr[] of positive integers. 
Find the third largest element in it. Return -1 if the third largest element is not found.

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.

"""

arr = [2, 4, 1, 3, 5, 19]

def get_third(array):
    #base cases

    #empty list is passed
    if array == []:
        return -1

        
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[i]:
                array[i],array[j] = array[j],array[i]
    # Sorting the list first
    # time O(n^2), space O(1) because sorting is IN PLACE

    return array[-3]


z = get_third(arr)
print(z)
