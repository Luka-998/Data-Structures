# Initially the same exercise as the "selection_sort" in the same repository, but with using the recursive apporach.

first_list = [8,2,4,9,3,16,255]
L = len(first_list)
# i will define find max function that i will call recursively during this task

# find me the first 
z = [41]

def find_max_id(arr):

    
    if len(arr) == 1:
        return 0

    next_id = find_max_id(arr[1:]) + 1

    if arr[0] > arr[next_id]:
        return 0
    else:
        return next_id

z = find_max_id(first_list)

print(f"Index of maximum number in this list is: {[z]}\nNumber: {first_list[z]}\n{'*'*15}")

