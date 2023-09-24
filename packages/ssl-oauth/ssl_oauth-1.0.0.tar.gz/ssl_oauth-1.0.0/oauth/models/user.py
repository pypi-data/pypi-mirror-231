import json

class User:
    id = ""
    first_name = ""
    second_name = ""
    username = ""
    email = ""

    def __init__(self, first_name, second_name, username, email, id):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.username = username
        self.email = email
    
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))