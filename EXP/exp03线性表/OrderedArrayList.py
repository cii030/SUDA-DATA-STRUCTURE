from DynamicArrayList import DynamicArrayList


class OrderedArrayList(DynamicArrayList):
    def __init__(self):
        super().__init__()

    def add(self, item):
        i = 0
        found = False
        while i < self._cur_len and not found:
            if item <= self._entry[i]:
                found = True
            else:
                i += 1
        if i == self._cur_len and not found:  # 加入的元素是顺序表中最大的元素，append到末尾
            self.append(item)
        if found:  # 相当于insert
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

    def insert(self, i, item):
        """按值插入元素,检查位置是否合理，合理就插入，不合理就抛出异常"""
        if not 0 <= i <= self._cur_len:
            raise IndexError('插入位置不合法')
        if i == 0:
            if item > self._entry[i]:
                raise IndexError('插入位置不合法（值不符合要求）')
        elif 0 < i <= self._cur_len:
            if not self._entry[i - 1] <= item <= self._entry[i]:
                raise IndexError('插入位置不合法（值不符合要求）')
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

    def replace(self, i, item):
        if not 0 <= i <= self._cur_len:
            raise IndexError('替换位置不合法')
        if i == 0:
            if item > self._entry[i+1] and self._cur_len != 1:
                raise IndexError('替换位置不合法（值不符合要求）')
        elif i == self._cur_len:
            if item < self._entry[i-1] and self._cur_len != 1:
                raise IndexError('替换位置不合法（值不符合要求）')
        elif 0 < i < self._cur_len:
            if not self._entry[i - 1] <= item <= self._entry[i + 1]:
                raise IndexError('替换位置不合法（值不符合要求）')
        self._entry[i] = item
