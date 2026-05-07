"""Given a list of numbers, the task is to find the product of all elements in the list. 
Multiplying all numbers in a list means multiplying each element together to get a single result."""
# escape 0 division 

arr = [14,2,1,2,3,0]
def get_multiply(x):
    res = 1
    for i in range(len(x)):
        if x[i] == 0:
            continue
        res *= x[i]
        
    return res
    
z = get_multiply(arr)
print(z)