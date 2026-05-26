# Leaders in an array

"""
Given an array arr[] of size n, the task is to find all the Leaders in the array.
An element is a Leader if it is greater than or equal to all the elements to its right side. 

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], 
therefore 17 is a leader. 5 is greater than all the elements to its right i.e.,
[2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
"""

array = [16,17,4,3,5,2]

def get_leader(arr):
    result = []
    for i in range(len(arr)):
        leader = arr[i]
        is_leader = True
        for j in range(i+1,len(arr)):   
            if arr[j] > leader:
                is_leader = False
        if is_leader:
            result.append(leader)
    return result
z = get_leader(array)
print(z)

"""

Assume that element checked by the outter loop is the leader:

in the inner loop, i check element after leader = arr[i]

IF some element to the right , is > than my current leader, set flag to false

then after the loop check if flag = True , append the leader


"""