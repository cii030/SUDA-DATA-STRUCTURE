from abc import ABCMeta, abstractmethod, ABC
import ctypes


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


class DynamicArrayList(AbstractList, ABC):
    def __init__(self, cap=0):
        """初始化一个空表"""
        super().__init__()
        self._cur_len = 0  # 线性表元素个数计数
        self._capacity = cap  # 默认数组容量
        self._entry = self._make_array(self._capacity)  # 存放所有表元素的数组

    def _make_array(self, cap):
        """保护方法，返回一个容量为cap的py_object数组"""
        return (cap * ctypes.py_object)()

    def empty(self):
        return self._cur_len == 0

    def __len__(self):
        """返回线性表中元素个数"""
        return self._cur_len

    def clear(self):
        self._capacity = 0
        self._cur_len = 0

    def append(self, item):
        """将元素item添加到线性表尾部"""
        if self._cur_len == self._capacity:  # 线性表的空间已用完
            if self._capacity == 0:
                cap = 4
            else:
                cap = 2 * self._capacity
            self._resize(cap)  # 给线性表扩容1倍空间
        self._entry[self._cur_len] = item  # 将item存储到表尾位置
        self._cur_len += 1  # 表长增1

    def _resize(self, cap):
        """将数组空间扩容至cap"""
        temp = self._make_array(cap)  # 生成新的更大的数组
        for k in range(self._cur_len):
            temp[k] = self._entry[k]
        del self._entry
        self._entry = temp
        self._capacity = cap

    def insert(self, i, item):
        """将元素item插入到表的i号位置"""
        if not 0 <= i <= self._cur_len:
            raise IndexError('插入位置不合法')
        if self._cur_len == self._capacity:  # 如果空间已经用完
            if self._capacity == 0:
                cap = 4
            else:
                cap = 2 * self._capacity
            self._resize(cap)  # 给线性表扩容1倍空间
        for j in range(self._cur_len, i, -1):  # 线性表尾部至i号位置所有元素后移
            self._entry[j] = self._entry[j - 1]
        self._entry[i] = item
        self._cur_len += 1

    def remove(self, i):
        if self.empty():
            raise Exception('underflow')
        if not 0 <= i < self._cur_len:
            raise IndexError('删除位置不合法')
        item = self._entry[i]
        for j in range(i, self._cur_len - 1):  # 将i号位置之后的元素前移
            self._entry[j] = self._entry[j + 1]
        self._cur_len -= 1
        return item

    def retrieve(self, i):
        if not 0 <= i < self._cur_len:
            raise IndexError('元素读取位置不合法')
        return self._entry[i]

    def replace(self, i, item):
        if not 0 <= i < self._cur_len:
            raise IndexError('元素写入位置不合法')
        self._entry[i] = item

    def contains(self, item):
        for i in range(self._cur_len):
            if self._entry[i] == item:
                return True
        return False

    def __str__(self):
        """将线性表转换成字符串，用于输出线性表所有元素"""
        elements = ' '.join(str(self._entry[c]) for c in range(self._cur_len))
        return elements

    def add(self, item):
        if self._cur_len == self._capacity:
            if self._capacity == 0:
                cap = 4
            else:
                cap = 2 * self._capacity
            self._resize(cap)
        i = 0
        found = False
        while i < self._cur_len and not found:
            if item <= self._entry[i]:
                found = True
                for j in range(self._cur_len, i, -1):
                    self._entry[j] = self._entry[j - 1]
                self._entry[i] = item
            i += 1
        if i == self._cur_len and not found:
            self._entry[i] = item
        self._cur_len += 1


if __name__ == '__main__':
    lst = DynamicArrayList()
    for k in range(1, 20, 2):
        lst.append(k)
    n = int(input())
    lst.add(n)
    print(lst)
"""时间复杂度O(n2)"""
