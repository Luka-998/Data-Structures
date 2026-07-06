"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

"""

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def get_result(arr):
    rows = len(arr) # number of rows is equal as the length of the matrix, because each 'list' inside matrix is 1 row
    cols = len(arr[0]) # number of cols = length of the row, because each number in list represents 1 column 

    top,bot = 0, rows - 1 # top row [1,3,5,7] , bot row [ 23,30,34,60]

    while top <= bot: # <= to find target row , and = to check if it even exist!
        middle_row = (top+bot)//2 # binary search

        if target > arr[middle_row][-1]: # check if target value is higher than the higest value in the row
            top+=1 # if yes , then from smaller row, go to bigger row
        elif target < arr[middle_row][0]: # checking if target value is lower than the lowest value in the current row
            bot -=1 # then we decrease search field by eliminating rows that have higher numbers than our target
        else:
            break
    if not (top<=bot):
        return False
    print(arr[middle_row]) # here is the row where the target is [1, 3, 5, 7]
    """
    Now the second binary search inside this row:
    """
    left = 0
    right = len(arr[middle_row]) - 1
    row = (bot+top) // 2

    while left <= right:
        mid_row = (left+right) // 2
        if target > arr[row][mid_row]:
            left+=1
        elif target < arr[row][mid_row]:
            right -=1
        else:
            return True
    return False
    


z = get_result(matrix)
print(z)