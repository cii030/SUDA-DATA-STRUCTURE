from AbstractList import AbstractList
from Node import Node


class LinkedList(AbstractList):
    def __init__(self):
        self._head = Node(None)

    def empty(self):
        return self._head.next is None

    def __len__(self):
        p = self._head.next
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def clear(self):
        p = self._head.next
        self._head.next = None  # 断开头结点和首结点
        while p is not None:
            q = p
            p = p.next
            del q

    def retrieve(self, i):
        if i < 0:
            raise IndexError('元素读取位置不合法，i小于0')
        p = self._head.next
        count = 0
        while p and count < i:
            p = p.next
            count += 1
        if p:
            return p.entry
        else:
            raise IndexError('读取位置不合法，i太大，不存在i号元素')

    def insert(self, i, item):
        if i < 0:
            raise IndexError('插入位置不合法，i值小于0')
        previous = self._head
        count = -1
        while previous and count < i-1:  # 定位previous到i-1号位置
            previous = previous.next
            count += 1
        if previous is None:
            raise IndexError('插入位置不合法，i太大')
        new_node = Node(item)
        new_node.next = previous.next
        previous.next = new_node

    def remove(self, i):
        if i < 0:
            raise IndexError('插入位置不合法，i值小于0')
        previous = self._head
        j = -1
        while previous and j < i - 1:
            previous = previous.next
            j += 1
        if previous is None:
            raise IndexError('删除位置不合法，不存在i-1号位置')
        current = previous.next
        if current is None:
            raise IndexError('删除位置不合法，不存在i号位置')
        previous.next = current.next
        item = current.entry
        del current
        return item

    def get_head(self):
        return self._head

    def traverse(self):
        res = []
        i = self._head.next
        while i:
            res.append(str(i.entry))
            i = i.next
        print(' '.join(res))

    def reverse(self):
        """链表反转"""
        p = self._head.next
        self._head.next = None
        while p:
            q = p.next
            p.next = self._head.next
            self._head.next = p
            p = q

    def __str__(self):
        res = []
        i = self._head.next
        while i:
            res.append(str(i.entry))
            i = i.next
        return ' '.join(res)

    def contains(self, item):
        p = self._head.next
        while p:
            if p.entry == item:
                return True
            p = p.next
        return False

    def replace(self, i, item):
        p = self._head.next
        count = 0
        while p and count < i:
            p = p.next
            count += 1
        if p is None:
            raise IndexError('i值不合法')
        p.entry = item
