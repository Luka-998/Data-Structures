# Python Program to Count Even and Odd Numbers in a List for unique occurences only! 
# output should be a dictionary with keys: odd , even 
# output should be of type list of tuple such as [(unique 1, even), (7, even), (5, even)]
x = [144,2,2,1,14,14,7,5]

def get_counts(array):
    odd = 0
    even = 0
    result_list = []
    

    unique_nums = [x for x in array if array.count(x)==1]

    for i in range(len(unique_nums)):
        if unique_nums[i] % 2:
            result_list.append(tuple(['even',unique_nums[i]]))
        else:
            result_list.append(tuple(['odd',unique_nums[i]]))
    return result_list


z = get_counts(x)
print(z)