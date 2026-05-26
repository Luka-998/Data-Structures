"""
Given an array, arr[] of positive integers. 
Find the third largest element in it. Return -1 if the third largest element is not found.

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.

"""
arr = [2, 4, 1, 3, 5]

def get_third(array):


    first = 0
    second = 0
    third = 0

    for i in range(len(array)):
        if array[i] > first:
            third = second
            second = first
            first = array[i]
            
    print(third)

z = get_third(arr)