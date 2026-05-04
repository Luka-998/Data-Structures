# Initially the same exercise as the "selection_sort" in the same repository, but with using the recursive apporach.

first_list = [8,2,4,9,3,67,16]

# Split the problem in smaller parts first:

# 1. Define the Base Case
# The recursion stops when the list has only one element. 
# In this case, the only available index is \(0\), which is naturally the index of the maximum element


# 2. Recursive Step and Comparison
# If the list has more than one element,
# recursively find the index of the maximum value in the rest of the list (from index \(1\) to \(n-1\)).

def get_max_id(arr):

    if len(arr) == 1:
        return 0
    
    rest_array = arr[1:]

    rest_array_max = get_max_id(rest_array)

    if arr[0] > rest_array[rest_array_max]:
        return 0
    else:
        return rest_array_max + 1
    

L = len(first_list)

# get max id within the full list n
# compare the max with the max of the sublist n -1
# swap

def selection_sort(arr,L):
    
    if L == 1:
        return arr[0]
    
    max_id = get_max_id(arr)
    
    arr[max_id],arr[-1] = arr[-1],arr[max_id]
    





z = selection_sort(first_list,L)
print(z)