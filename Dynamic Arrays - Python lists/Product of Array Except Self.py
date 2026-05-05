"""
Implement a function foo(List[int]) -> List[int] which, given a list of integers, 
returns a new list such that each element at index i of the new list is the 
product of all the numbers in the original array except the one at i.
"""

def except_self_product(arr:list):
    
    result_array = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if j!=i:
                result_array[i] *=arr[j]

    return result_array





z = except_self_product([3,2,1])
print(z)