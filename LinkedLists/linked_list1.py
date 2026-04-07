class SinglyLinked():
    def __init__(self,val,next=None):
        self.val= val
        self.next = next
    def __str__(self):
        return str(self.val)


Head = SinglyLinked(1)
A = SinglyLinked(2)
B = SinglyLinked(3)
C = SinglyLinked(7)

Head.next = A
A.next=B
B.next = C
