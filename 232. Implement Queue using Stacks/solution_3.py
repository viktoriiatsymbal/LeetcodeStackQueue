"""
Implement Queue using Stacks."""

class Node:
    """
    Node class."""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    """
    Stack class."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Returns True if the stack is empty."""
        return self.head is None

    def push(self, item):
        """
        Pushes new element to the peek of the stack."""
        self.head = Node(item, self.head)

    def pop(self):
        """
        Pops top element from the stack."""
        item = self.head.item
        self.head = self.head.next
        return item

    def peek(self):
        """
        Returns the peek of the stack."""
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:
    """
    MyQueue class."""
    def __init__(self):
        self.enqueueing_stack = Stack()
        self.dequeueing_stack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.enqueueing_stack.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.dequeueing_stack.is_empty():
            while not self.enqueueing_stack.is_empty():
                self.dequeueing_stack.push(self.enqueueing_stack.pop())
        return self.dequeueing_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.dequeueing_stack.is_empty():
            while not self.enqueueing_stack.is_empty():
                self.dequeueing_stack.push(self.enqueueing_stack.pop())
        return self.dequeueing_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.enqueueing_stack.is_empty() and self.dequeueing_stack.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
