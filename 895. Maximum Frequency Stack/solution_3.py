"""
Maximum Frequency Stack."""

from collections import deque

class FreqStack(object):
    """
    FreqStack class."""
    def __init__(self):
        self.stack_of_val = deque()
        self.stack_of_frequency = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.stack_of_val:
            self.stack_of_val.append(val)
            self.stack_of_frequency.append(self.stack_of_val.count(val)+1)
        else:
            self.stack_of_val.append(val)
            self.stack_of_frequency.append(1)

    def pop(self):
        """
        :rtype: int
        """
        index_counter = -1
        max_freq = max(self.stack_of_frequency)
        self.stack_of_val.reverse()
        self.stack_of_frequency.reverse()
        max_index = self.stack_of_frequency.index(max_freq)
        for ele in self.stack_of_val:
            index_counter += 1
            if index_counter == max_index:
                self.stack_of_val.remove(ele)
                self.stack_of_frequency.remove(max_freq)
                item_popped = ele
                break
        self.stack_of_val.reverse()
        self.stack_of_frequency.reverse()
        return item_popped

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
