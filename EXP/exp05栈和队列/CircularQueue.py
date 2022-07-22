class CircularQueue:
    def __init__(self, cap=10):
        self._capacity = cap
        self._entry = [None for x in range(0, self._capacity)]
        self._front = 0
        self._rear = self._capacity - 1

    def empty(self):
        return self._front == (self._rear + 1) % self._capacity

    def __len__(self):
        return (self._rear - self._front + 1 + self._capacity) % self._capacity

    def append(self, item):
        if self._front == (self._rear + 2) % self._capacity:  # 判断队列是否已满
            self.resize(2 * len(self._entry))
        self._rear = (self._rear + 1) % self._capacity
        self._entry[self._rear] = item

    def resize(self, cap):
        old = self._entry  # 用old指示原空间
        self._entry = [None] * cap  # 用entry
        p = self._front  # p在原空间中移动
        k = 0  # k在新空间中移动
        while p != self._rear:
            self._entry[k] = old[p]
            p = (p + 1) % self._capacity
            k += 1
        self._entry[k] = old[self._rear]  # 最后一个队尾元素的复制
        self._front = 0
        self._rear = k
        self._capacity = cap

    def serve(self):
        if self.empty():
            return None
        else:
            item = self._entry[self._front]
            self._front = (self._front + 1) % self._capacity
            return item

    def retrieve(self):
        if self.empty():
            return None
        else:
            return self._entry[self._front]

    def clear(self):
        self._front = 0
        self._rear = self._capacity - 1

    def traverse(self):
        if self.empty():
            return None
        for i in range(self._front, self._rear + 1):
            if self._entry[i]:
                print(self._entry[i], end=' ')
        print()
