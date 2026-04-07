# Double linked list
# One direction traversal po petlji

class DoubleLink():
    def __init__(self,val,next=None,prev=None):
        self.val= val
        self.next= next
        self.prev = prev
    def __str__(self):
        return str(self.val)

head = DoubleLink(1)
A = DoubleLink(10)
B = DoubleLink(20)
C = DoubleLink(30)
tail = DoubleLink(100)

head.next = A
A.prev = head

A.next = B
B.prev = A

B.next = C
C.prev = B

C.next = tail
tail.prev = C
        
    
curr = head
last = tail

while curr:
    print(curr)
    curr = curr.next

while last:
    print(last)
    last = last.prev


print('---'*10)

def make_new_head(head,val):
    new_node = DoubleLink(val,next=head)
    head.prev = new_node
    return new_node

z = make_new_head(head,3000)
print(f'New head is {z}')
print('--'*5)

curr = z
while curr:
    print(curr)
    curr = curr.next
    

# Jos ovo je ostalo
def insert_after(node,val):
