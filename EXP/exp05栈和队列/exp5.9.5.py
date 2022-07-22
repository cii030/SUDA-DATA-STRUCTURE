from CircularQueue import CircularQueue


def candy(n: str):
    top = CircularQueue()
    for i in n:
        top.append(int(i))
    branch = []  # 用列表模拟stack
    lake = []
    current_num = 1
    while len(lake) != len(n):
        if top.empty() and branch[-1] != current_num:
            print('---------------------------------')
            return '结论：失败'
        if branch and branch[-1] == current_num:  # 先判断分支（栈）中第一个元素是否符合条件
            current_num += 1
            lake.append(branch.pop())
        else:
            item = top.serve()
            if item == current_num:
                lake.append(item)
                current_num += 1
            else:
                branch.append(item)
        print('---------------------------------')
        print('branch', branch)
        print('lake', lake)
    print('---------------------------------')
    return '结论：成功'


if __name__ == '__main__':
    n = input('输入序列：')
    print(candy(n))
