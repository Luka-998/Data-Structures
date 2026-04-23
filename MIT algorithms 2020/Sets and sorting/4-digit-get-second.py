# for the 4 value number, get 2nd value 
# example num: 1241 
# result = 2 

x = str(input())

def get_num(X):
    while len(str(X))<=3:
        print("Number must have at least 4 digits!")
        X = int(input())
    y = int(X) // 100 # remove last 2 digits

    return y%10

result = get_num(x)
print(result)