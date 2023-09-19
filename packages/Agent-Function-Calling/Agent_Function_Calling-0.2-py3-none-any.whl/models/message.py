class Message:
    VALID_ROLES = ["system", "assistant", "user", "function"]

    def __init__(self, role, content, name=None):
        if role not in self.VALID_ROLES:
            raise ValueError(f"Invalid role '{role}'. Valid roles are: {', '.join(self.VALID_ROLES)}")
        
        if role == "function" and name is None:
            raise ValueError("When role is 'function', a 'name' attribute is required.")
        
        self.role = role
        self.content = content
        self.name = name

    def __repr__(self):
        if self.role == "function":
            return f"<Message(role='{self.role}', name='{self.name}', content='{self.content}')>"
        return f"<Message(role='{self.role}', content='{self.content}')>"

    def to_dict(self):
        """Convert the Message object to a dictionary."""
        data = {
            "role": self.role,
            "content": self.content
        }
        if self.role == "function":
            data["name"] = self.name
        return data

    @staticmethod
    def from_dict(data):
        """Create a Message object from a dictionary."""
        return Message(data["role"], data["content"], data.get("name"))

