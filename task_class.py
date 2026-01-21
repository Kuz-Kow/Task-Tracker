import time

class task:
    ID = 1
    def __init__(self, id, description, completed = "todo", created_at = time.asctime(), updated_at = time.asctime()):
        self.id = id
        self.__class__.ID += 1
        self.description = description
        self.completed = completed
        self.created_at = created_at
        self.updated_at = updated_at