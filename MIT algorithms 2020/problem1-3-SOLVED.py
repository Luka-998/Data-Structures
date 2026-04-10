class LinkedList():
    def __init__(self,value,next=None):
        self.value = str(value)
        self.next = next
    def __str__(self):
        return str(self.value)


Head = LinkedList('Branch')
B = LinkedList('Luka')
C = LinkedList('Steph')
D = LinkedList('Who?')
E = LinkedList('March')
F = LinkedList('Joe')

Head.next = B
B.next = C
C.next = D
D.next = E
E.next = F


def reorder_students(head):
    curr = head

    count = 0
    prev = None

    while curr:
        count+=1
        curr = curr.next
    n = count//2
    first_half = head
    for _ in range(n-1):
        #print(first_half)
        first_half = first_half.next
    second_half = first_half.next
    first_half.next = None #otkacena prva lista

    curr = second_half
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    first_half.next = prev
    return head
        
        
r = reorder_students(Head)
    
