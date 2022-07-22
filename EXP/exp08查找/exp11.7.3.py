from Record import Record
import time
import random


class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root = None


class BStree(BinaryTree):
    def recursive_search_bst(self, sub_root, target, times, flag):
        if not sub_root:
            flag = False
            return times
        else:
            times += 1
            if sub_root.data.key == target:
                return times
            elif sub_root.data.key < target:
                return self.recursive_search_bst(sub_root.right, target, times+1,flag)
            else:
                return self.recursive_search_bst(sub_root.left, target, times+1,flag)

    def search(self, target):
        flag = True
        result = self.recursive_search_bst(self._root, target, 0, flag)
        if flag:
            return result
        else:
            return result

    def search_and_insert(self, sub_root, new_data):
        if sub_root is None:
            sub_root = BinaryNode(new_data)
            return sub_root
        elif new_data == sub_root.data:
            raise Exception('重复')
        elif new_data < sub_root.data:
            sub_root.left = self.search_and_insert(sub_root.left, new_data)
        else:
            sub_root.right = self.search_and_insert(sub_root.right, new_data)
        return sub_root

    def insert(self, new_data):
        self._root = self.search_and_insert(self._root, new_data)


if __name__ == '__main__':
    lst = [i for i in range(1, 200, 2)]  # 列表中放1-199的100个奇数
    BStree1 = BStree()
    for i in lst:  # 按升序建立二叉查找树1
        record = Record(i)
        BStree1.insert(record)
    random.shuffle(lst)  # 随机打乱lst
    BStree2 = BStree()
    for i in lst:
        record = Record(i)
        BStree2.insert(record)
    print('升序二叉查找树查找在成功情况下的绝对运行时间：', end='')
    start1 = time.perf_counter()
    times1 = 0
    for i in range(10000):
        k1 = random.randrange(1, 200, 2)
        times = BStree1.search(k1)
        times1 += times
    end1 = time.perf_counter()
    print(str(end1 - start1))
    print(f'升序二叉查找树查找ASLsucc={times1 / 10000}')
    print('升序二叉查找树查找在失败情况下的绝对运行时间：', end='')
    start2 = time.perf_counter()
    times2 = 0
    for i in range(10000):
        k1 = random.randrange(0, 199, 2)
        times = BStree1.search(k1)
        times2 += times
    end2 = time.perf_counter()
    print(str(end2 - start2))
    print(f'升序二叉查找树查找ASLunsucc={times2 / 10000}')
    print('随机二叉查找树查找在成功情况下的绝对运行时间：', end='')
    start3 = time.perf_counter()
    times3 = 0
    for i in range(10000):
        k1 = random.randrange(1, 200, 2)
        times = BStree2.search(k1)
        times3 += times
    end3 = time.perf_counter()
    print(str(end3 - start3))
    print(f'随机二叉查找树查找ASLsucc={times3 / 10000}')
    print('随机二叉查找树查找在失败情况下的绝对运行时间：', end='')
    start4 = time.perf_counter()
    times4 = 0
    for i in range(10000):
        k1 = random.randrange(0, 199, 2)
        times = BStree2.search(k1)
        times4 += times
    end4 = time.perf_counter()
    print(str(end4 - start4))
    print(f'随机二叉查找树查找ASLunsucc={times4 / 10000}')