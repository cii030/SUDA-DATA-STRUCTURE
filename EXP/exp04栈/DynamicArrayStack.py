from AbstractStack import AbstractStack


class DynamicArrayStack(AbstractStack):
    increment = 10  # 栈的容量增量

    def __init__(self, init_size=0):
        super().__init__()
        self._capacity = init_size  # 栈容量赋值为初始容量
        self._entry = [None for x in range(0, self._capacity)]
        self._top = -1  # 栈顶位置初始化为-1

    def empty(self):
        return self._top == -1

    def __len__(self):
        return self._top + 1  # 栈的长度为栈顶位置加1

    def push(self, item):
        if self._top >= self._capacity - 1:
            self._resize()  # 栈原空间已用完，调用resize扩容
        self._top += 1
        self._entry[self._top] = item

    def _resize(self):
        self._capacity += self.increment
        temp = [None for x in range(0, self._capacity)]
        for i in range(0, self._capacity - self.increment):
            temp[i] = self._entry[i]  # 原来的栈元素一次复制到新列表中
        self._entry = temp

    def pop(self):
        if self.empty():
            raise Exception('栈为空')
        else:
            item = self._entry[self._top]
            self._top -= 1
            return item

    def get_top(self):
        if self.empty():
            raise Exception('栈为空')
        else:
            return self._entry[self._top]

    def traverse(self):
        print('[', end='')
        for i in range(self._top + 1):
            print(self._entry[i], end=' ')
        print(']')

