# Count how many times, a target number appears in the list

numbers = [2, 5, 2, 8, 2, 3]
target = 2



def count_occurrences(numbers, target):
    if numbers == []:
        return 0

    count_rest = count_occurrences(numbers[1:], target)

    if numbers[0] == target:
        return 1 + count_rest
    else:
        return count_rest
    
result = count_occurrences(numbers,target)
print(result)