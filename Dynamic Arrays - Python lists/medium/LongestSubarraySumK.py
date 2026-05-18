# Longest Subarray with Sum K

# given the list of numbers (Z) 
# return the length of the longest continue subarray with the sum K

arr = [10, 5, 2, 7, 1, 9]
# k = 15
# output = 4 
# [5,2,7,1]

def get_Longest(array):

    k = 15
    max_len = 0
    for i in range(len(array)): 
        
        current = 0
        
        for j in range(i,len(array)):
            current+=array[j]
            if current == k:
                current_len = j+1 - i
                if current_len > max_len:
                    max_len = current_len
    return max_len

                         



result = get_Longest(arr)
print(result)


# time = O(n**2)
# space = O(1)