class Student:
    def __init__(self, id, name, birth_year, class_id):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.class_id = class_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "class_id": self.class_id
        }

    @staticmethod
    def from_dict(data):
        return Student(data["id"], data["name"], data["birth_year"], data["class_id"])


class Class:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_dict(data):
        return Class(data["id"], data["name"])
