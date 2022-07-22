from CircularQueue import CircularQueue


def testCircularQueue(n, lst: CircularQueue):
    if n == 'empty':
        print(lst.empty())
    elif n == 'len':
        print(lst.__len__())
    elif n == 'clear':
        lst.clear()
        lst.traverse()
    elif n == 'serve':
        lst.serve()
        lst.traverse()
    elif n == 'retrieve':
        print(lst.retrieve())
    elif n == 'append':
        item = int(input('请输入想要入队的元素item: '))
        lst.append(item)
        lst.traverse()
    else:
        print('未知的指令')


if __name__ == '__main__':
    lst = CircularQueue()
    while 1:
        n = input('请输入想要实现的方法（按Q或q退出程序）: ')
        if n == 'q' or n == 'Q':
            print('游戏停止')
            break
        else:
            testCircularQueue(n, lst)
