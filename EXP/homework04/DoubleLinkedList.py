class Node:
    def __init__(self, data):
        self.next = None
        self.prior = None
        self.entry = data
        self.freq = 0


class DoubleLinkedList:
    def __init__(self):
        self._head = Node(None)

    def append(self, item):
        p = self._head
        new_node = Node(item)
        while p.next:
            p = p.next
        p.next = new_node
        new_node.prior = p

    def __str__(self):
        res = []
        p = self._head.next
        while p:
            res.append(str(p.entry))
            p = p.next
        return ' '.join(res)

    def locate(self, x):
        p = self._head.next
        while p:
            if p.entry == x:
                p.freq += 1
                break
            p = p.next
        p.prior.next = p.next  # 删除p节点
        p.next.prior = p.prior
        q = self._head.next  # 对p节点按freq值重新插入
        while q:
            if q.freq < p.freq:
                break
            q = q.next
        pre_node = q.prior
        pre_node.next = p
        p.prior = pre_node
        p.next = q
        q.prior = p


if __name__ == '__main__':
    lst = DoubleLinkedList()
    for i in range(5):
        lst.append(i)
    print(lst)
    lst.locate(1)
    print(lst)
    lst.locate(2)
    print(lst)
    lst.locate(2)
    print(lst)