class Line:
    def __init__(self, name, status, message, timestamp):
        self.name = name
        self.status = status
        self.message = message
        self.timestamp = timestamp

    def __repr__(self):
        st = f"Name: {self.name} Time: {self.timestamp} Status: {self.status}"
        return st

    def to_csv(self):
        return [self.name, self.timestamp, self.status, self.message]
