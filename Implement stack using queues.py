from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue for stack elements
        self.q2 = deque()  # Auxiliary queue for temporary storage during push

    def push(self, x: int) -> None:
        # To maintain LIFO order, when pushing, add new element to q2
        # then move all elements from q1 to q2, and finally swap q1 and q2.
        # This makes the newly pushed element the "front" of q1.
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Pop is simply removing the front element from q1
        if not self.q1:
            return None # Or raise an error, depending on desired behavior for empty stack
        return self.q1.popleft()

    def top(self) -> int:
        # Top is simply looking at the front element of q1
        if not self.q1:
            return None # Or raise an error
        return self.q1[0]

    def empty(self) -> bool:
        # The stack is empty if q1 is empty
        return not self.q1

# Example Usage (from the problem description's example 1):
# myStack = MyStack()
# myStack.push(1)
# myStack.push(2)
# myStack.top()    # Returns 2
# myStack.pop()    # Returns 2
# myStack.empty()  # Returns False
