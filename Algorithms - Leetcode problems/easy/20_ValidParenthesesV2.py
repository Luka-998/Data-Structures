"""
20. Valid Parentheses
Attempted
Easy


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""
s = "()]"


def get_valid(arr):

    brackets = {'(':')','{':'}','[':']'}
    stack = []
    if len(arr) == 1:
        return False
    for s in arr:
        for k,v in brackets.items():
            if s == k:
                stack.append(s)
            if s == v:
                if not stack:
                    return False
                if brackets[stack[-1]] != s:
                    return False
                else:
                    stack.pop()           
                
    if stack == []:
        return True
    else:
        return False

p = get_valid(s)

print(p)