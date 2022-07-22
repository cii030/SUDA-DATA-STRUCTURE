from abc import ABCMeta, abstractmethod


class AbstractList(metaclass=ABCMeta):
    """抽象表类，metaclass=ABCMeta表示AbstractList类为ABCMeta的子类"""

    @abstractmethod
    def __init__(self):
        """初始化线性表"""

    @abstractmethod
    def empty(self):
        """判断表是否为空"""

    @abstractmethod
    def __len__(self):
        """返回表中元素的个数"""

    @abstractmethod
    def clear(self):
        """清空表"""

    @abstractmethod
    def insert(self, i, item):
        """在表中i号位置插入元素item"""

    @abstractmethod
    def remove(self, i):
        """删除i号位置的元素"""

    @abstractmethod
    def retrieve(self, i):
        """获取i号位置的元素"""

    @abstractmethod
    def replace(self, i, item):
        """用item替换表中i号位置的元素 """

    @abstractmethod
    def contains(self, item):
        """判断表中是否包含元素item"""

    @abstractmethod
    def traverse(self):
        """输出表中所有元素"""


class Node:
    def __init__(self, data, next=None):
        self.entry = data
        self.next = next


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
        while previous and count < i - 1:  # 定位previous到i-1号位置
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

    def replace(self, i, item):
        pass

    def contains(self, item):
        pass

    def traverse(self):
        pass

    def find_lastk(self, k):
        if k <= 0:
            raise IndexError('k值非法')
        fast = self._head
        slow = self._head
        for i in range(k):
            fast = fast.next
            if fast is None:
                raise IndexError('k值非法')
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.entry


if __name__ == '__main__':
    lst = LinkedList()
    k = int(input())
    n = input()
    nums = list(map(int, n.split()))
    for i in range(len(nums)):
        lst.insert(i, nums[i])
    try:
        print(lst.find_lastk(k))
    except IndexError:
        print('Not Found')

