class sequence:
    def __init__(self, start, n):
        self.start = start
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            self.start = self.start + 1
            return self.start
        else:
            raise StopIteration

    def _advance(self):
        return self.start + 1


class arithmetic_sequence(sequence):  # 等差数列
    def __init__(self, start, n, increment):
        super().__init__(start, n)
        self.increment = increment

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            self.start = self.start + self.increment
            return self.start
        else:
            raise StopIteration

    def _advance(self):
        return self.start + self.increment


class proportional_sequence(sequence):  # 等比数列
    def __init__(self, start, n, base):
        super().__init__(start, n)
        self.base = base

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            self.start = self.start * self.base
            return self.start
        else:
            raise StopIteration

    def _advance(self):
        return self.start * self.base


class fibonacci_sequence(sequence):  # 斐波那契数列
    def __init__(self, start, second, n):
        super().__init__(start, n)
        self.first = start
        self.second = second

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            self.first, self.second = self.second, self.first + self.second
            return self.first
        else:
            raise StopIteration

    def _advance(self):
        return self.first + self.second


b = fibonacci_sequence(1, 5, 6)
for i in b:
    print(i, end=' ')
