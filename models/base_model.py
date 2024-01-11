import uuid
import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        self.__dict__ = {"__class__": self.__class__.__name__, **self.__dict__}
        return self.__dict__
