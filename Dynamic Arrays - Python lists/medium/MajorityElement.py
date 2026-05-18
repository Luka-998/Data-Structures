# Majority Element
"""
Given an array arr[] of size n, 
find the element that appears more than ⌊n/2⌋ times. If no such element exists, return -1.

Examples:

    Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
    Output: 1
    Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

    Input: arr[] = [7]
    Output: 7
    Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

"""

array = [1, 1, 2, 1, 3, 5, 1]

def find_major(arr):

    n = len(arr)

    if len(arr) == 1:
        return arr[0]
    
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
        if count > n //2:
            return arr[i]

p = find_major(array)
print(p)


print(15/2)
print(15//2)
print(15%2)