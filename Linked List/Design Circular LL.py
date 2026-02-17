class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.cq = [-1] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.cq[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.cq[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.cq[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front