import time
import json


class task:
    
    
    def __init__(self, description, completed = "todo", created_at = time.asctime(), updated_at = time.asctime()):
        self.id = None
        self.description = description
        self.completed = completed
        self.created_at = created_at
        self.updated_at = updated_at 
    
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=5)