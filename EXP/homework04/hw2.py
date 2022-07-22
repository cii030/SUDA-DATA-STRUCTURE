class Node:
    def __init__(self, data, next=None):
        self.entry = data
        self.next = next


class OrderedLinkedList:
    """有序单链表（递增）"""
    def __init__(self):
        self._head = Node(None)

    def append(self, item):
        if self._head.next is None:
            new_node = Node(item)
            self._head.next = new_node
        else:
            p = self._head
            while p.next and item > p.next.entry:
                p = p.next
            new_node = Node(item)
            new_node.next = p.next
            p.next = new_node

    def get_head(self):
        return self._head

    def __str__(self):
        res = []
        i = self._head.next
        while i:
            res.append(str(i.entry))
            i = i.next
        return ' '.join(res)


def difference(a: OrderedLinkedList, b: OrderedLinkedList) -> OrderedLinkedList:
    p = a.get_head().next
    q = b.get_head().next
    res = OrderedLinkedList()
    while p and q:
        if p.entry < q.entry:
            res.append(p.entry)
            p = p.next
        elif p.entry > q.entry:
            q = q.next
        else:
            p = p.next
            q = q.next
    while p:   # 判断完q表后p表剩余的都是差集中的元素
        res.append(p.entry)
        p = p.next
    return res


if __name__ == '__main__':
    n1 = input()
    lst1 = list(map(int, n1.split()))
    n2 = input()
    lst2 = list(map(int, n2.split()))
    a = OrderedLinkedList()
    for i in lst1:
        a.append(i)
    b = OrderedLinkedList()
    for i in lst2:
        b.append(i)
    print(difference(a, b))