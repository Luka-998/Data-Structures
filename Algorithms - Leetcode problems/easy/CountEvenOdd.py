# Python Program to Count Even and Odd Numbers in a List
# output should be a dictionary with keys: odd , even 
# values are number of occurences in the list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_counts(array):
    odd = 0
    even = 0
    for i in range(len(array)):
        if array[i] % 2 !=0:
            even +=1
        else:
            odd +=1
    return {'even':even,'odd':odd}
            
        
z = get_counts(a)
print(z)

