def binarySearch(x: list, target: int):
    low = 0
    high = len(x) - 1
    if low > high:
        return False
    while low < high:
        mid = (low + high) // 2
        current = x[mid]
        if target <= current:
            high = mid
        else:
            low = mid + 1
    current = x[low]
    if current == target:
        return True
    else:
        return False


def search(x: list, k: int):
    lst = []
    for i in range(len(x) // 2):  # 只要遍历一半，避免重复
        num1 = x[i]
        target = k - num1
        if binarySearch(x, target):  # 二分查找k-num1在列表中
            dif = target - num1
            lst.append((num1, target, dif))
    lst.sort(key=lambda i: i[2], reverse=True)  # 将查找到的值按dif递减排序
    res = (lst[0][0], lst[0][1])
    return res


if __name__ == '__main__':
    x = list(map(int, input().split()))
    k = int(input())
    print(search(x, k))