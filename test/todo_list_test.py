import unittest
from datetime import date
from models.todo_list import TodoList
from models.todo_item import TodoItem
from models.user import User


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.valid_TodoList = TodoList()
        self.valid_TodoItem = TodoItem("test", "name")
        for x in range(1):
            self.valid_TodoList.add_item(self.valid_TodoItem)

    def test_valid_user(self):
        self.assertTrue(self.valid_TodoList.is_valid())
