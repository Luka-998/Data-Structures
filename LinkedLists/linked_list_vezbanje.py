# Linked list

class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

head = SinglyNode(1)
A = SinglyNode(10)
B = SinglyNode(20)

head.next = A
A.next = B

# Traverse the list
curr = head
while curr:
    #print(curr)
    curr = curr.next
# curr se stavlja na pocetak tj head.
# gura se do kraja liste, dok ne izbaci None , au medjuvremenu printuje svaki linked list


# nadji node
def search(val):
    curr = head
    while curr:
        if curr.val == val:
            print('val found')
            return val
            break
        else:
            print(f"No match at: {curr}")
        curr = curr.next
    


find = search(20)
print(find)
