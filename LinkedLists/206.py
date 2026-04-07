# 1-2-3 - None
# reverse it

class LinkedList():
    def __init__(self,value,next=None,reverse=None):
        self.value = value
        self.next = next
        self.reverse = reverse

    def __str__(self):
        return str(self.value)


head = LinkedList(1)
A = LinkedList(2)
B = LinkedList(3)

head.next = B

# head - A - B 

# B - A - head

def reverse(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next # A
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

r = reverse(head)
print(r)
