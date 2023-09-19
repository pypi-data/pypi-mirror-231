import random

class Random:

    def __init__(self):
        self.value = 0
        self.round_value = 0

    def randint(self, start, end):
        self.value = random.randint(start, end)
        return self.value

    def uniform(self, start, end):
        self.value = random.uniform(start, end)
        return self.value

    def round(self, num):
        self.round_value = round(num, 2)
        return self.round_value
