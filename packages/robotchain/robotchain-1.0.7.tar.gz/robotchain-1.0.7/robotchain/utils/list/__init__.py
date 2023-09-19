import json

class List:

    def __init__(self):
        self.list = []

    def init(self):
        self.list = []

    def set(self, list_data):
        self.list = json.loads(list_data)
        return self.list
