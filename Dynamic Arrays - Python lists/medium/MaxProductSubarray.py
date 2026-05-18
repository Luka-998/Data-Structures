# Maximum Product Subarray

"""
Given an array arr[] consisting of positive, negative, and zero values, 
find the maximum product that can be obtained from any contiguous subarray of arr[]. 

--- 
Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

"""

array = [-2, 6, -3, -10, 0, 2]


def get_product(arr):

    max_product = arr[0]

    for i in range(len(arr)):
        current_product = 1
        for j in range(i,len(arr)):
            current_product *=arr[j]
            if current_product > max_product:
                max_product = current_product
                
    return max_product

            

p = get_product(array)
print(p)