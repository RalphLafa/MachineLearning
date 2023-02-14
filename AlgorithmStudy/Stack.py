class LinkedNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class stack_head():
    def __init__(self):
        self.head = LinkedNode(0)
        self.size = 0

    def push(self, x: int):
        self.size += 1
        newNode = LinkedNode(x)
        newNode.next = self.head.next
        self.head.next = newNode

    def pop(self):
        if self.head.next:
            self.size -= 1
            ans = self.head.next.val
            self.head.next = self.head.next.next
            return ans
        else:
            return "stack is empty"

    def getSize(self):
        return self.size

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
