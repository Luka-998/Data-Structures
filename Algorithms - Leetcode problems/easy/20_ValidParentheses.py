# 20. Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
---------
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

"""

strs ="){"
def get_valid(strs):

    if len(strs) == 1:
        return False
    
    mapper = {'(':')','{':'}','[':']'}
    stack = []

    if len(strs) == 2:
        if mapper[strs[0]] != mapper[strs[1]]:
            return False

    if len(strs) % 2 !=0:
        return False
  
    i = 0
    while i < len(strs):
        for key,value in mapper.items():
            if strs[i] == key:
                stack.append(strs[i]) # cim se doda jedan u stack, proveravam stack -> sledeci # 
            if strs[i] == value: # prva zatvorena zagrada - > 1.( 2.( 3.) 4.] = > (( )]
                if mapper[stack[-1]] == strs[i]:
                    print(mapper[stack[-1]])
                    print(strs[i])
                    stack.pop()
                    print(stack)
                else:
                    return False
        i+=1            
    if stack == []:
        return True
    return False


       

d = get_valid(strs)
print(d)


