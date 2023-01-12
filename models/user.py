import re
from datetime import date

from models import TodoList


class User:
    def __init__(self, first_name, last_name, email, uuid, password, birthdate, ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.uuid: str = uuid
        self.password: str = password
        self.birthdate: date = birthdate
        self.todolist: TodoList = TodoList()

    def is_valid(self):
        if not self.first_name:
            return False

        if not self.last_name:
            return False

        if not self.email:
            return False

        if not self.uuid:
            return False

        if not re.match(r"^(?=.[a-z])(?=.[A-Z])(?=.*\d)[a-zA-Z\d]{8,40}$", self.password):
            return False

        if (date.today() - self.birthdate).days/365 < 13:
            return False

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False

        return True
