# Count Subarrays with Sum Greater Than K
# given array arr = [1, 2, 3, 4]
# k = 5

# return continued subarrays that has sum > k and number of subarrays
array = [1,2,3,4]

def get_arrays(arr,k):

    total_count = 0
    result = []
    for i in range(len(arr)):
        current_sum = 0
        current_sub = []
        for j in range(i,len(arr)):
            current_sum += arr[j]
            if current_sum > k:
                total_count+=1
                current_sub.append(arr[i:j+1])
        if not current_sub == []:
            result.append(current_sub)
    print(result)
    return total_count
z = get_arrays(array,5)
print(z)


        
