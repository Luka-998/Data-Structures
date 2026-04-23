# for number X , calculate first bigger round number 
# example: 1343 -> 1350 
# example: 760 -> 770
#example: 4 -> 10
import math
in_number = int(input())


def get_res(x):
    """
    idea: remove the last digit by the whole number division. That way: 2//10, 0 , increment by 1 and * 10
    """
    y = x //10

    y +=1

    return y * 10

result = get_res(in_number)
print(result)