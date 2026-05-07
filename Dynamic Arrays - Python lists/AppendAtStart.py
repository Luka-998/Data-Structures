# Perform Append at Beginning of List - Python

"""
The task of appending an element
to the beginning of a list involves adding a new item at the start of an existing list, 
shifting the other elements to the right. 
"""

arr = [1, 2, 3, 4]
x = 0
def get_append(array,x):

    # using the slice method

    result = [x] + array[:]
    print(result)
z = get_append(arr,x)