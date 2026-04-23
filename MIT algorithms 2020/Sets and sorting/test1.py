# for the whole number > 9 , get the last but one value

X = int(input())

def get_val(x):
    y = x // 10 # removing the last number
    return y% 10 # get the last but one

res  = get_val(X)
print(f"Starting num: {X}\nLast but one num: {res}")