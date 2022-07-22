class ArrayStack:
    def __init__(self):
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

    def traverse(self):
        res = ''
        for i in self._entry:
            res += str(i)
        return res


def string_deal(s: str) -> str:
    stack = ArrayStack()
    for i in s:
        if i == stack.get_top():
            stack.pop()
        else:
            stack.push(i)
    return stack.traverse()


if __name__ == '__main__':
    string = input()
    print(string_deal(string))
