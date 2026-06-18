# 15. 3Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.



Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

# My idea:

# 1st thing is to sort the array
# use first number in the array as the offset value
# offset + 1 in the array will be the low pointer
# array - 1 will be the high pointer
# excluding the offset, i calcualate the sum of (low,high) 
# if offset + sum(low,high) = 0 => the triplet

nums = [-1,0,1,2,-1,-4]


def get_triplets(arr):
    
    sorted = []
    min_value = arr[0]

    for i in range(len(arr)): # bubble sort O(n^2) time complexity
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    sorted = arr
    
    i = 0 
    triplet = []

    for i in range(len(arr)):
        if arr[i] > 0: # if offset number is greater than 0, all others number are also greater , which means it will break the constraint sum == 0:
            break
        elif i > 0 and arr[i]== arr[i-1]:
            continue
        low,high = i+1,len(arr) -1
        while low < high:
            summ = arr[i] + arr[low] + arr[high]
            if summ == 0:
                triplet.append([arr[i],arr[low],arr[high]])
                low,high = low+1,high-1
                while low < high and arr[low]==arr[low-1]:
                    low+=1
                while low < high and arr[high] == arr[high+1]:
                    high -=1
            elif summ < 0:
                low +=1
            else:
                high -=1

    return triplet 


    
        

z = get_triplets(nums)
print(z)