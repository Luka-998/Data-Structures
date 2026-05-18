# Majority Element II -  Elements occurring more than ⌊n/3⌋ times

"""
Given an array arr[] consisting of n integers, 
find all the array elements which occurs more than floor(n/3) times.
Note: The returned array of majority elements should be sorted.

Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
Output: [1, 2]
Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

"""

arr = [2, 2, 3, 1, 3, 2, 1, 1]

def get_major(arr):

    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0]]
    
    n = len(arr)
    remember = {}
    keys_list = []
    for i in range(len(arr)):
        counter = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                counter +=1

        if counter > n // 3:
            remember[arr[i]] = counter
    for keys,_ in remember.items():
        keys_list.append(keys)

    if len(keys_list) == 2:
        if keys_list[0]>keys_list[1]:
            keys_list[0],keys_list[1] = keys_list[1],keys_list[0]
    return keys_list
            

z = get_major(arr)
print(z)