from datetime import date
from datetime import datetime


class TodoItem:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.timestamp = datetime.now()

    def is_valid(self):
        if not self.name:
            return False
        if len(str(self.text)) > 1000:
            return False
        return True
