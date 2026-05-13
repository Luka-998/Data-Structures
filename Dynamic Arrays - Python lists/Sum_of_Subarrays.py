# Sum of all Subarrays

"""
Given an integer array arr[],
compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.

Input: arr[] = [1, 4, 5, 3, 2]
Output: 116
Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

"""
array = [1,2,3]
def get_sum(arr):
    total = 0

    for i in range(len(arr)):
        temp = 0
        for j in range(i,len(arr)):
            temp+=arr[j]
            total +=temp
    print(total)

z = get_sum(array)