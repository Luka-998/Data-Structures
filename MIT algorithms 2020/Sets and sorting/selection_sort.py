
first_list = [8,2,4,9,3]

def selection_sort(first_list):
    
    for i in range(len(first_list)): # 0 (8) -> 1 (2) -> 2 -> 3 
        max_id = 0 
        for j in range(len(first_list)-i): # 0 1 2 3 4 (8 2 4 9 3) - > 0 1 2 3 ( 8 2 4 9)-> 0 1 2 -> 0 1
            if first_list[j] > first_list[max_id]:
                max_id = j
        first_list[j],first_list[max_id] = first_list[max_id],first_list[j]
    return first_list

              
                
ss = selection_sort(first_list)
print(ss)

"""
sanity check
if i == 0:
    print(j)
elif i ==1:
    print(j)        
elif i == 2:
    print(j)
"""