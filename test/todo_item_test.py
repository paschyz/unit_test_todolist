import unittest
from datetime import date

from models.todo_item import TodoItem


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.valid_TodoItem = TodoItem("name", "textfsefes")

    def test_valid_user(self):
        self.assertTrue(self.valid_TodoItem.is_valid())
