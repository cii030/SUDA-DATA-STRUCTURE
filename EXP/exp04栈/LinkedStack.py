class StackNode:
    def __init__(self, data, link=None):
        self.entry = data
        self.next = link


class LinkedStack:
    def __init__(self):
        self._top = None

    def empty(self):
        return self._top is None

    def __len__(self):
        p = self._top
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def push(self, item):
        new_top = StackNode(item, self._top)
        self._top = new_top

    def pop(self):
        if self.empty():
            return None
        else:
            old_top = self._top
            self._top = self._top.next
            item = old_top.entry
            del old_top
            return item

    def get_top(self):
        if self.empty():
            return None
        else:
            return self._top.entry

    def traverse(self):
        p = self._top
        while p:
            print(p.entry, end=' ')
            p = p.next
        print()
