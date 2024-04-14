"""
Implement Stack using Queues."""

class Node:
    """
    Node class."""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    """
    Queue class."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Returns True if the queue is empty."""
        return self.front is None

    def add(self, item):
        """
        Adds new element to the top of the queue."""
        node = Node(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def pop(self):
        """
        Pops top element from the front of the queue."""
        item = self.front.item
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return item

    def top(self):
        """
        Returns the top of the queue."""
        return self.front.item

    def __len__(self):
        count = 0
        current = self.front
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        cur = self.front
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'front -> '+ s+'<- rear'

class MyStack(object):
    """
    MyStack class."""
    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.first_queue:
            self.second_queue.add(self.first_queue.pop())
        self.first_queue.add(x)
        while self.second_queue:
            self.first_queue.add(self.second_queue.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.first_queue.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.first_queue.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.first_queue.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
