class User:
    def __init__(self, firstname, name):
        self.firstname = firstname
        self.name = name

    def is_valid(self):
        if not self.firstname:
            return False
        if not self.name:
            return False
        if any(str(chr).isdigit() for chr in self.firstname):
            return False
        if str(self.name).isdigit():
            return False

        return True
