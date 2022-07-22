from AbstractStack import AbstractStack


class ArrayStack(AbstractStack):
    """列表实现"""
    def __init__(self):
        super().__init__()
        self._entry = []

    def empty(self):
        return self._entry == []

    def __len__(self):
        return len(self._entry)

    def push(self, item):
        self._entry.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._entry.pop()

    def get_top(self):
        if self.empty():
            return None
        return self._entry[-1]