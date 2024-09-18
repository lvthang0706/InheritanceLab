class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.append(item)
    def pop(self):
        return self.data.pop() if not self.is_empty() else None
    def peek(self):
        return self.data[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.data) == 0
    def __str__(self):
        return ', '.join(self.data)
