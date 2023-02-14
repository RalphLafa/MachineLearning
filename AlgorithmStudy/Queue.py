class LinkedNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class myQueue():
    def __init__(self):
        self.head = LinkedNode(0)
        self.tail = LinkedNode(0)
        self.head.prev = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = self.tail
        self.size = 0

    def enqueue(self, x: int):
        self.size += 1
        newNode = LinkedNode(x)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        
    def dequeue(self):
        if self.head.next != self.tail:
            self.size -= 1
            ans = self.tail.prev.val
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            return ans
        else:
            return "Queue is empty"

    def getSize(self):
        return self.size

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False