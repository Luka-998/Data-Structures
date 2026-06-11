"""
Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.


"""

import pandas as pd
import numpy as np


df = pd.DataFrame({'nums':[1,1,1,2,1,1,2,4,4,4,4,4,2]})
df.insert(0,'id',range(1,len(df)+1))
#print(df)

def get_consecutive(df):
    numbers_array = df['nums'].to_numpy()
    counter = 1
    consecutives = set()
    previous = 0

    for i in range(1,len(numbers_array)):
        previous = numbers_array[i-1]
        if numbers_array[i] == previous:
            counter+=1
            if counter >=3:
                consecutives.add(numbers_array[i])

        else:
            counter = 1
    
    return pd.DataFrame(list(consecutives),columns=['consecutiveNumbers'])
p = get_consecutive(df)
print(p)