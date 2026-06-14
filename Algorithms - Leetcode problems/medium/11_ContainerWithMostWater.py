# 11. Container With Most Water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

"""

height = [1,8,6,2,5,4,8,3,7]

def get_container(arr):
    max_water = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] < arr[right]:
            current_water = arr[left] * (right - left)
            left+=1
            if  current_water > max_water:
                max_water = current_water
        elif arr[right]<= arr[left]:
            current_water = arr[right] * (right - left)
            right-=1
            if current_water > max_water:
                max_water = current_water
                print(max_water)
                

    return max_water
        
        


z = get_container(height)   
#print(z)


