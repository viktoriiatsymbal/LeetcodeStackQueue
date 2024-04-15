"""
Maximum Frequency Stack."""

from collections import deque

class FreqStack(object):
    """
    FreqStack class."""
    def __init__(self):
        self.dict_of_occurrence = {}
        self.max_frequency = 0
        self.dict_of_occurrence_grouped = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.dict_of_occurrence:
            self.dict_of_occurrence[val] = 0
        self.dict_of_occurrence[val] += 1
        frequency = self.dict_of_occurrence[val]
        if frequency not in self.dict_of_occurrence_grouped:
            self.dict_of_occurrence_grouped[frequency] = deque()
        self.dict_of_occurrence_grouped[frequency].append(val)
        self.max_frequency = max(self.max_frequency, frequency)

    def pop(self):
        """
        :rtype: int
        """
        item_to_pop = self.dict_of_occurrence_grouped[self.max_frequency].pop()
        self.dict_of_occurrence[item_to_pop] -= 1
        if not self.dict_of_occurrence_grouped[self.max_frequency]:
            del self.dict_of_occurrence_grouped[self.max_frequency]
            self.max_frequency -= 1
        return item_to_pop

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
