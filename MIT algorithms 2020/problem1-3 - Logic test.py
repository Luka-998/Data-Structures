# problem 1-3 - Logic of the reverse only
"""

Problem 1-4. Jen & Berry’s
Jen drives her ice cream truck to her local elementary school at recess. All the kids rush to line up in front of her truck. Jen is overwhelmed with the number of students (there are 2n of them), so she calls up her associate, Berry, to bring his ice cream truck to help her out. Berry soon arrives and parks at the other end of the line of students. He offers to sell to the last student in line, but the other students revolt in protest: “The last student was last! This is unfair!”
The students decide that the fairest way to remedy the situation would be to have the back half of the line (the n kids furthest from Jen) reverse their order and queue up at Berry’s truck, so that the last kid in the original line becomes the last kid in Berry’s line, with the (n+1)st kid in the original line becoming Berry’s first customer.
(a)
Given a linked list containing the names of the 2n kids, in order of the original line formed in front of Jen’s truck (where the first node contains the name of the first kid in line), describe an O(n)-time algorithm to modify the linked list to reverse the order of the last half of the list. Your algorithm should not make any new linked list nodes or instantiate any new non-constant-sized data structures during its operation.

"""

class linked():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)

A = linked(1)
B = linked(10)
C = linked(100)
D = linked(200)
E = linked(300)
A.next = B
B.next = C
C.next = D
D.next = E

L = []

curr = A
prev = None
while curr:
    a_next = curr.next
    curr.next = prev
    prev = curr
    curr = a_next
    print(prev)
