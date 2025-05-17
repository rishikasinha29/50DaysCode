class MyQueue:

    def __init__(self):
        self.stack1 = [] # For enqueueing
        self.stack2 = [] # For dequeueing

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return -1 #Or raise an exceotion for empty queue

    def peek(self) -> int:
        """
        Returns the element at the front of the queue without removing it.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        return -1

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
