from models import TodoItem
from typing import List
from datetime import datetime, timedelta


class TodoList():

    def __init__(self) -> None:
        self.todo_items: List[TodoItem] = []
        self.capacity: int = 10
        self.warn_treshold: int = 8

    def add_item(self, item: TodoItem) -> None:
        if (len(self.todo_items) >= 0):
            for todo_item in self.todo_items:
                if datetime.now() - todo_item.timestamp < timedelta(minutes=30):
                    raise Exception("Added an item 30 min ago or less !")

        self.todo_items.append(item)
        if self.should_warn():
            print("Warning: List is almost full!")
        if len(self.todo_items) >= self.capacity:
            raise Exception("List is full!")

    def remove_item(self, item: TodoItem) -> None:
        self.todo_items.remove(item)

    def should_warn(self) -> bool:
        return len(self.todo_items) == self.warn_treshold

    def is_valid(self) -> bool:
        if not self.todo_items:
            return False
        if len(self.todo_items) > self.capacity:
            return False
        if len(self.todo_items) < 0:
            return False

        return True
