from Node import Node


class CircularLinkedlist:
    def __init__(self):
        self._head = Node(None)
        self._head.next = self._head

    def empty(self):
        return self._head.next == self._head

    def __len__(self):
        p = self._head.next
        count = 0
        while p != self._head:
            count += 1
            p = p.next
        return count

    def insert(self, i, item):
        if i < 0:
            raise IndexError('invalid i')
        count = -1
        p = self._head
        while p.next != self._head and count < i - 1:
            p = p.next
            count += 1
        if count == i - 1:
            new_node = Node(item)
            new_node.next = p.next
            p.next = new_node
        else:
            raise IndexError('invalid i')

    def clear(self):
        p = self._head.next
        self._head.next = self._head
        while p.next != self._head:
            q = p
            p = p.next
            del q

    def retrieve(self, i):
        if i < 0:
            raise IndexError('invalid i')
        p = self._head.next
        count = 0
        while p.next != self._head and count < i:
            count += 1
            p = p.next
        if count == i:
            return p.entry
        else:
            raise IndexError('invalid i')

    def __str__(self):
        res = []
        i = self._head.next
        while i != self._head:
            res.append(str(i.entry))
            i = i.next
        return ' '.join(res)

    def remove(self, i):
        if i < 0:
            raise IndexError('invalid i')
        p = self._head.next
        q = self._head
        count = 0
        while p.next != self._head and count < i:
            p = p.next
            count += 1
            q = q.next
        if p == self._head:
            raise IndexError('invalid i')
        q.next = p.next
        value = p.entry
        del p
        return value

    def traverse(self):
        res = []
        i = self._head.next
        while i != self._head:
            res.append(str(i.entry))
            i = i.next
        print(' '.join(res))

    def reverse(self):
        p = self._head.next
        self._head.next = self._head
        while p != self._head:
            q = p.next
            p.next = self._head.next
            self._head.next = p
            p = q

    def contains(self, item):
        p = self._head.next
        while p != self._head:
            if p.entry == item:
                return True
            p = p.next
        return False

    def replace(self, i, item):
        p = self._head.next
        count = 0
        while p != self._head and count < i:
            p = p.next
            count += 1
        if p == self._head:
            raise IndexError('i值不合法')
        p.entry = item

if __name__ == '__main__':
    lst = CircularLinkedlist()
