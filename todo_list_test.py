import unittest
from datetime import date
from models.todo_list import TodoList
from models.user import User


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.valid_TodoList = TodoList()

    def test_valid_user(self):
        self.assertTrue(1)
