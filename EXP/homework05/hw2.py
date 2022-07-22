import math


class ArrayStack:
    """列表实现"""

    def __init__(self):
        self._entry = []

    def empty(self):
        return self._entry == []

    def __len__(self):
        return len(self._entry)

    def push(self, item):
        self._entry.append(item)

    def pop(self):
        if self.empty():
            return None
        return self._entry.pop()

    def get_top(self):
        if self.empty():
            return None
        return self._entry[-1]


def isPrime(n: int) -> bool:
    if n == 1:
        return False
    else:
        maxNumber = int(math.sqrt(n))
        for i in range(2, maxNumber + 1):
            if n % i == 0:
                return False
        return True


def decompose(n: int):
    stack = ArrayStack()
    res = f'{str(n)}='
    while n > 1:
        divisor = 2
        found = False
        while divisor <= n and not found:
            if isPrime(divisor) and n % divisor == 0:
                stack.push(divisor)
                n = n // divisor
                found = True
            divisor += 1
    lst = []
    while not stack.empty():
        lst.append(str(stack.pop()))
    res += '*'.join(lst)
    print(res)


if __name__ == '__main__':
    n = int(input())
    decompose(n)
