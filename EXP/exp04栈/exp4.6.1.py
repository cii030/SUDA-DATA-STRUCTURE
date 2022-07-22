from DynamicArrayStack import DynamicArrayStack
from LinkedStack import LinkedStack


def test_DynamicArrayStack():
    x = DynamicArrayStack()
    print('顺序栈类')
    print('现栈是否为空：(empty)')
    print(x.empty())
    print('加入元素4&22:(push)')
    x.push(4)
    x.push(22)
    print('现栈为：')
    x.traverse()
    print('表长：(len)')
    print(x.__len__())
    print('获取顶层元素：(get_top)')
    print(x.get_top())
    print('删除元素：(pop)')
    x.pop()
    print('现栈为：')
    x.traverse()
    print('现栈是否为空：(empty)')
    print(x.empty())

def test_LinkedStack():
    x = LinkedStack()
    print('链栈类')
    print('现栈是否为空：(empty)')
    print(x.empty())
    print('加入元素4&22:(push)')
    x.push(4)
    x.push(22)
    print('现栈为：')
    x.traverse()
    print('表长：(len)')
    print(x.__len__())
    print('获取顶层元素：(get_top)')
    print(x.get_top())
    print('删除元素：(pop)')
    x.pop()
    print('现栈为：')
    x.traverse()
    print('现栈是否为空：(empty)')
    print(x.empty())

def score(x: list) -> int:
    stack = DynamicArrayStack()
    res = 0
    for i in x:
        if i == 'D':
            new_value = stack.get_top() * 2
            stack.push(new_value)
        elif i == 'C':
            stack.pop()
        elif i == '+':
            value1 = stack.pop()
            value2 = stack.get_top()
            value3 = value1 + value2
            stack.push(value1)
            stack.push(value3)
        else:
            stack.push(int(i))
    while not stack.empty():
        res += stack.pop()
    return res


if __name__ == '__main__':
    test_LinkedStack()
