from Record import Record
import time
import random


class SearchTableList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def empty(self):
        return not self.data

    def insert(self, record):
        self.data.append(record)

    def remove(self, key):
        r = Record(key)
        self.data.remove(r)

    def traverse(self):
        for r in self.data:
            print(r.key, end='')

    def sequentialSearch(self, target):
        """有序表的顺序查找算法"""
        times = 0
        for i in range(len(self.data)):
            current = self.data[i].key
            times += 1  # 判断的等于时次数+1
            if current == target:
                return times
            times += 1  # 判断＞或者＜次数+1
            if current > target:
                return times
        return times

    def binarySearch1(self, target):
        """不识别相等的二分查找"""
        low = 0
        high = len(self.data) - 1
        times = 0
        if low > high:
            return times
        while low < high:
            times += 1
            mid = (low + high) // 2
            current = self.data[mid].key
            if target <= current:
                high = mid
            else:
                low = mid + 1
        current = self.data[low].key
        if current == target:
            return times
        else:
            return times

    def recBinarySearch1(self, target, low, high, times):
        if low > high:
            return times
        elif low == high:
            current = self.data[low].key
            if current == target:
                return times
            else:
                return times
        else:
            mid = (low + high) // 2
            current = self.data[mid].key
            if target <= current:
                return self.recBinarySearch1(target, low, mid, times + 1)
            else:
                return self.recBinarySearch1(target, mid + 1, high, times + 1)

    def recursiveBinarySearch1(self, target):
        return self.recBinarySearch1(target, 0, len(self.data) - 1, 0)

    def binarySearch2(self, target):
        """识别相等的二分查找"""
        times = 0
        low = 0
        high = len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            current = self.data[mid].key
            times += 1  # 识别相等+1次
            if target == current:
                return times
            times += 1  # 识别大于或者小于+1次
            if target < current:
                high = mid - 1
            else:
                low = mid + 1
        return times


if __name__ == '__main__':
    n = 100
    m = 10000
    searchTable1 = SearchTableList()
    for i in range(1, 2 * n, 2):
        record = Record(i)
        searchTable1.insert(record)
    print('有序表的顺序查找在成功情况下的绝对运行时间：',end='')
    start1 = time.perf_counter()
    times1 = 0
    for i in range(m):
        k1 = random.randrange(1, 2 * n, 2)  # 随机生成1~2n-1的奇数
        times = searchTable1.sequentialSearch(k1)
        times1 += times
    end1 = time.perf_counter()
    print(str(end1-start1))
    print(f'有序表的顺序查找ASLsucc={times1/m}')
    print('有序表的顺序查找在失败情况下的绝对运行时间：', end='')
    start2 = time.perf_counter()
    times2 = 0
    for i in range(m):
        k1 = random.randrange(0, 2 * n - 1, 2)  # 随机生成0~2n-2的偶数
        times = searchTable1.sequentialSearch(k1)
        times2 += times
    end2 = time.perf_counter()
    print(str(end2-start2))
    print(f'有序表的顺序查找ASLunsucc={times2 / m}')
    print('有序表的非递归二分查找1在成功情况下的绝对运行时间：', end='')
    start3 = time.perf_counter()
    times3 = 0
    for i in range(m):
        k1 = random.randrange(1, 2 * n, 2)
        times = searchTable1.binarySearch1(k1)
        times3 += times
    end3 = time.perf_counter()
    print(str(end3-start3))
    print(f'有序表的非递归二分查找1ASLsucc={times3 / m}')
    print('有序表的非递归二分查找1在失败情况下的绝对运行时间：', end='')
    start4 = time.perf_counter()
    times4 = 0
    for i in range(m):
        k1 = random.randrange(0, 2 * n - 1, 2)  # 随机生成0~2n-2的偶数
        times = searchTable1.binarySearch1(k1)
        times4 += times
    end4 = time.perf_counter()
    print(str(end4 - start4))
    print(f'有序表的非递归二分查找1ASLunsucc={times4 / m}')
    print('有序表的非递归二分查找2在成功情况下的绝对运行时间：', end='')
    start5 = time.perf_counter()
    times5 = 0
    for i in range(m):
        k1 = random.randrange(1, 2 * n, 2)
        times = searchTable1.binarySearch2(k1)
        times5 += times
    end5 = time.perf_counter()
    print(str(end5 - start5))
    print(f'有序表的非递归二分查找2ASLsucc={times5 / m}')
    print('有序表的非递归二分查找2在失败情况下的绝对运行时间：', end='')
    start6 = time.perf_counter()
    times6 = 0
    for i in range(m):
        k1 = random.randrange(0, 2 * n - 1, 2)  # 随机生成0~2n-2的偶数
        times = searchTable1.binarySearch2(k1)
        times6 += times
    end6 = time.perf_counter()
    print(str(end6 - start6))
    print(f'有序表的非递归二分查找2ASLunsucc={times6 / m}')
    print('有序表的递归二分查找1在成功情况下的绝对运行时间：', end='')
    start7 = time.perf_counter()
    times7 = 0
    for i in range(m):
        k1 = random.randrange(1, 2 * n, 2)
        times = searchTable1.recursiveBinarySearch1(k1)
        times7 += times
    end7 = time.perf_counter()
    print(str(end7 - start7))
    print(f'有序表的递归二分查找1ASLsucc={times7 / m}')
    print('有序表的递归二分查找1在失败情况下的绝对运行时间：', end='')
    start8 = time.perf_counter()
    times8 = 0
    for i in range(m):
        k1 = random.randrange(0, 2 * n - 1, 2)  # 随机生成0~2n-2的偶数
        times = searchTable1.recursiveBinarySearch1(k1)
        times8 += times
    end8 = time.perf_counter()
    print(str(end8 - start8))
    print(f'有序表的递归二分查找1ASLunsucc={times8 / m}')

