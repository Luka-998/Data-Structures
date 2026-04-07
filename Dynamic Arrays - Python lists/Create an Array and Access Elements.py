#Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
# Sample Output:
'''
1
3
5
7
9
Access first three items individually
1
3
5
'''

def make_arr(num):
    arr =[]
    for i in range(1,num+1,2):
        arr.append(i)
    return arr
z = make_arr(10)
print(z)

print(z[0]) #first
print(z[1]) #2nd
print(z[2]) #3rd
        
