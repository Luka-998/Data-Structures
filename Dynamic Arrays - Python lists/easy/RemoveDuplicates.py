# Remove Duplicates from a List
"""
Given a list that may contain repeated values, the task is to remove duplicate elements and keep only unique ones.
For Example: Input: [1, 2, 2, 3, 4, 4, 5], Output: [1, 2, 3, 4, 5].
Not allowed: set() 

"""

# define the base case first
# if list has 1 element , return list[0]

arr = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(array):
    result = []

    if len(array) == 1:
        return [array]
    
    for i in range(len(array)):
        is_seen = False
        for j in range(i): # Checking all the elements before i -> in first iteration of i , it's 0
            if array[i] == array[j]:
                is_seen=True
                break
        if not is_seen:
            result.append(array[i])
             
            
    return result
z = remove_duplicates(arr)
print(z)