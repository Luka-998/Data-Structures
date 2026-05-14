# Rotate an Array by d - Counterclockwise or Left

"""
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {3, 4, 5, 6, 1, 2}

"""

# Space O(1) 
# Time O(n*d), complex time. If d was a size of d -> O(n**2)
    
arr = [1, 2, 3, 4, 5, 6]
arr2 = [1,2,3]
d = 2
d2 = 4

def rotate_array(arr):

    for i in range(d2):
        left = arr.pop(0)
        arr.append(left)  
    return arr

z = rotate_array(arr2)
print(z)


"""
After poppin the 1st element from the array, and appending it to the end of the array,
I need again first element. It is always 0!

First error was trying to swap arr[i],arr[-1] because i has values of 0,1 for d=2 , which is wrong. 
In first iteration i would swap 1st and last element and in the second iteration i would swap 2nd and last element.


"""