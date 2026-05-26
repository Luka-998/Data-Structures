# Sort an array in wave form

"""
Given a sorted array arr[] of integers (in ascending order), 
rearrange the elements in-place to form a wave-like array.
An array is said to be in wave form if it satisfies the following pattern:
 arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...

In other words, every even-indexed element should be greater than 
or equal to its adjacent odd-indexed elements (if they exist).

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

"""

array = [1,2,4,5,3]
array.sort()
# 1 [2 3 4 5]
def wave_Array(arr):

    even_index = None
    odd_index = None

    if arr[0] % 2 == 0:
        even_index = 0
    else: 
        odd_index = 0

  
    for i in range(1,len(arr)-1):
        if arr[i]%2 ==0:
            even_index = i
            odd_index = i-1
            arr[odd_index],arr[even_index] = arr[even_index],arr[odd_index]
        odd_index = i +2
        
    return arr



        

z = wave_Array(array)
        


print(z)