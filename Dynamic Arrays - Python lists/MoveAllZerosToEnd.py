"""
Move all Zeros to End of Array

Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

example:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]


"""

array =  [1, 2, 0, 4, 3, 0, 5, 0]

def move_zeros(arr):
    found_zero = False
    zero_index = 0
    for i in range(len(arr)):
        if arr[i] == 0 and not found_zero:
            found_zero = True
            zero_index = i
        if arr[i] != 0 and found_zero:
            arr[zero_index],arr[i] = arr[i],arr[zero_index] 
            zero_index +=1
    return arr
  
        
z = move_zeros(array)

print(z)

"""
Failures in this exercise:

1) I initialized zero_index inside the loop, which resets at each iteration...

2) I did not capture correctly, non zero element.

3) Be more aware of the state. When 0 is encountered, i label it's index and state = True. The first next non-zero element is swapped with this zero
    but zero_index is incremented by 1 , because that zero is now +1 index to the right.

"""