# Given a list of numbers, the task is to find the smallest element in that list.

arr = [8, 3, 1, 9, 5, -15]

def get_smallest(x):
    smallest = x[0]
    for i in range(len(x)):
        if x[i] < smallest:
            smallest = x[i]
    return smallest

result = get_smallest(arr)
print(result)