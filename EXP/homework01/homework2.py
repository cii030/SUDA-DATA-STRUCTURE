import math


def prime(n: int) -> bool:
    if n == 1:
        return False
    else:
        maxNumber = int(math.sqrt(n))
        for i in range(2, maxNumber+1):
            if n % i == 0:
                return False
        return True


def guess(x: int):
    if x <= 0 or x % 2 != 0:
        print(0)
    else:
        lst = []
        res = 0
        for i in range(1, x // 2):
            if prime(i):
                lst.append(i)
        for i in lst:
            if prime(int(x - i)):
                print(i)
                print(x-i)
                res += 1
                break
        if res == 0:
            print(0)


n = int(input())
guess(n)
