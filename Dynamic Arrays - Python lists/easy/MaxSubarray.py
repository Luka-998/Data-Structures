# Maximum Subarray Sum - Kadane's Algorithm

"""
Given an integer array arr[], find the subarray 
(containing at least one element) which has the maximum possible sum, and return that sum.

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

"""
array = [2, 3, -8, 7, -1, 2, 3]

def get_res(arr):

    max_sum = arr[0]

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i,(len(arr))):
            current_sum +=arr[j]
            if current_sum>max_sum:
                max_sum = current_sum
    return max_sum

z = get_res(array)
print(z)
