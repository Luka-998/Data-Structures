# Problem Session 1

"""
Problem 1-2. Given a data structure D supporting the four first/last sequence operations:
D.insert first(x), D.delete first(), D.insert last(x), D.delete last(),
each in O(1) time, describe algorithms to implement the following higher-level operations in terms
of the lower-level operations. Recall that delete operations return the deleted item.
(a) swap ends(D): Swap the first and last items in the sequence in D in O(1) time.
(b) shift left(D, k): Move the first k items in order to the end of the sequence n D
in O(k) time. (After, the kth item should be last and the (k + 1)st item should be first.)
"""


# swap_ends(D)

d = [0,12,14,22,16]

def swap_ends(d):
    d[0],d[-1]=d[-1],d[0]
    return d

s = swap_ends(d)
#print(s)


#O(1)time / O(1) space


# b) shift left(D, k): Move the first k items in order to the end of the sequence n D
# in O(k) time. (After, the kth item should be last and the (k + 1)st item should be first.)
print(f"This is: {d}")

def shift_left(d,k):
    if k < 1 or k > len(d)-1:
        return None
    for i in range(k):
        x = D.delete_first(d)
        x1 = D.insert_last(x)
    return d
z = shift_left(d,2)
print(z)
