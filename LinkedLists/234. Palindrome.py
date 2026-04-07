# Given the head of a singly linked list, return true if it is a or false otherwise.

class LinkedList():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)


head = LinkedList(1)
A = LinkedList(10)
B = LinkedList(10)
C = LinkedList(1)

head.next = A
A.next = B
B.next = C


curr = head
list1 = []
while curr:
#    print(curr)
    list1.append(curr)
    curr= curr.next



for i in list1:
    if list1[i] == :
        print('yes')
