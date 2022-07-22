class Node:
    def __init__(self, data, next=None):
        self.entry = data
        self.next = next


class LinkedList:
    def __init__(self):
        self._head = Node(0)

    def append(self, item):
        new_node = Node(item)
        new_node.next = self._head.next
        self._head.next = new_node

    def traverse(self):
        res = []
        i = self._head.next
        while i:
            res.append(str(i.entry))
            i = i.next
        print(' '.join(res))

    def insertion_sort(self):
        if not self._head.next:
            return
        curr = self._head.next.next  # curr为待插入的元素
        last_sorted = self._head.next  # 有序序列的最后一位
        while curr:
            if last_sorted.entry <= curr.entry:
                last_sorted = last_sorted.next
            else:
                prev = self._head  # prev为插入curr的前一个结点
                while prev.next.entry <= curr.entry:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next


if __name__ == '__main__':
    lst = LinkedList()
    plst = list(map(int, input().split()))
    for i in plst:
        lst.append(i)
    lst.insertion_sort()
    lst.traverse()
