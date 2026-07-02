"""
27. Remove Element
Easys  


Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""
# FIRST ATTEMPT (1)
nums = [3,2,2,3]
val = 3

# objective: 1) remove occurences of val in nums [3,2,2,3] -> [2,2] #inplace!

# objective: 2) return length of current array w/o val

# first pointer will be starting point of array, next pointer will be second element
# if first pointer is val , increment it so next starting point is next element
# if this element != val, i move second pointer forward until i hit val index,here i make changes to my current array, and set first pointer to 
# first next number, until the end of the array repeat this behaviour

def remove_element(arr,val):

    first = 0
    second = 1

    for i in range(len(arr)): # 3 -> val = 3
        if arr[first]==val: # true
            first+=1 # first pointer at index 1
            second+=1 # second pointer at index 2
            # while loop to check while second is not val:
                # true - increment second 
                # arr[i] = arr[first:second+1] # may expect out of bound failure?

z = remove_element(nums,val)

# SECOND ATTEMPT (2)

def second_attempt(arr,val): # [3,2,2,3]

    first = 0 # pointer to indicate where to put element which is not equal to val

    for i in range(len(arr)): # index 1 - > first 2 value
        if arr[i] != val:
            arr[first] = arr[i]
            first+=1
        else:
            continue
    return len(arr[:first])

p = second_attempt(nums,val)
print(p)

# This case works , lets check nums = [0,1,2,2,3,0,4,2], val = 2
nums_2 = [0,1,2,2,3,0,4,2]
val_2 = 2

x = second_attempt(nums_2,val_2)
print(x)

#2nd attempt -> WORKING!