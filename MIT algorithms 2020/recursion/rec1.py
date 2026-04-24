# Write a recursive function that given an input n sums all nonnegative integers up to n.
"""

n = 5
def fact(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
z = fact(n)
print(z)



# fibbonaci number

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
p = fibo(n)
print(f'Fibo: {p}')


# Write a code that calculates sum of all numbers in the list
"""
numbers = [3, 5, 2, 8]

def get_sum(num):
    if num == []:
        return 0
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + get_sum(num[1:])


z = get_sum(numbers)
print(z)