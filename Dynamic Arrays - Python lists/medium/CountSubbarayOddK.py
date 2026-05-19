# Count Subarrays with Exactly K Odd Numbers

# return number of continued subarrays  that have exactly K odd number of elements
# result:
# [1, 1, 2, 1] 1:3 count
# [1, 2, 1, 1] 1: 3 count
arr = [1, 1, 2, 1, 1]
k = 3

test1= [2, 4, 6]
k1 = 2

test2 = [2, 2, 1, 2, 1]
k2 = 2
def get_array_k(array,k):

    total_count = 0
    for i in range(len(array)):
        odd_count = 0
        for j in range(i,len(array)):
            if array[j] % 2 !=0:
                odd_count+=1
            if odd_count == k:
                total_count+=1
    return total_count

z = get_array_k(test2,k2)
print(z)
                    


            
