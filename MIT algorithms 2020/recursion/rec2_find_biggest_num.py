# write a recursive function that find the biggest number in the given list of nums

zz = [3, 5, 2, 8]

def find_max(numbers):
    if numbers == []: # if list is empty return None
        return None 
    
    if len(numbers) == 1: # if list length is 1 return first element
        return numbers[0]
    
    max_list = find_max(numbers[1:]) # make a smaller list 1: to the end

    if numbers[0] > max_list: # check if first element is larger than any element in the sublist
        return numbers[0]  # if yes return that element
    else:
        return max_list # if NO -> Then return that sliced list [5,2,8] and go again

result = find_max(zz)
    
print(result)

