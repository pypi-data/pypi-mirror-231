import time
import json
from .loging import Loging
from .random import Random
from .list import List

class Utils:

    def __init__(self, framework):
        self._framework = framework
        self.log = Loging()
        self.random = Random()
        self.list = List()
        self.time = time
        self.json = json
