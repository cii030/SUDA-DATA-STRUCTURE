from DynamicArrayStack import DynamicArrayStack

operator = {'+', '-', '*', '/', '#', '(', ')'}


def tokens(text: str):
    i, t_len = 0, len(text)
    while i < t_len:
        if text[i].isspace():
            i += 1
        elif text[i] in operator:
            yield text[i]
            i += 1
        else:
            j = i + 1
            while j < t_len and not text[j].isspace() and text[j] not in operator:
                #  操作数用科学记数法表示，且遇到负指数
                if (text[j] == 'e' or text[j] == 'E') and j + 1 < t_len and text[j + 1] == '-':
                    j += 1
                j += 1
            yield text[i:j]
            i = j
    yield '#'


def postfix(postfix_ex):
    stack = DynamicArrayStack()
    for m in tokens(postfix_ex):
        if m not in operator:
            stack.push(float(m))
            stack.traverse()
        else:
            if m == '#':
                output = stack.pop()
                if not stack.empty():
                    raise Exception('操作数过多')
                return output
            opnd2 = stack.pop()
            if stack.empty():
                raise Exception('运算符过多')
            opnd1 = stack.pop()
            op = m
            res = 0
            if op == '+':
                res = opnd1 + opnd2
            elif op == '-':
                res = opnd1 - opnd2
            elif op == '*':
                res = opnd1 * opnd2
            elif op == '/':
                if opnd2 == 0:
                    raise ZeroDivisionError('除数为0')
                res = opnd1 / opnd2
            stack.push(res)
            stack.traverse()


def calc_infix(infix_ex):
    priority = {'*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 2, '#': 1}
    opnd = DynamicArrayStack()  # 存放操作数
    optr = DynamicArrayStack()  # 存放算符
    optr.push('#')
    for m in tokens(infix_ex):
        if m not in priority:
            opnd.push(m)
        elif m == '(':
            optr.push(m)
        else:
            theta1 = optr.get_top()  # 栈顶算符
            theta2 = m  # 当前算符
            while theta1 != '#' or theta2 != '#':
                if priority[theta1] < priority[theta2]:
                    optr.push(theta2)
                    break
                elif theta1 == '(' and theta2 == ')':
                    optr.pop()
                    break
                else:
                    theta1 = optr.pop()
                    opnd2 = float(opnd.pop())
                    if opnd.empty():
                        raise Exception('运算符过多')
                    opnd1 = float(opnd.pop())
                    res = 0
                    if theta1 == '+':
                        res = opnd1 + opnd2
                    elif theta1 == '-':
                        res = opnd1 - opnd2
                    elif theta1 == '*':
                        res = opnd1 * opnd2
                    elif theta1 == '/':
                        if opnd2 == 0:
                            raise ZeroDivisionError('除数为0')
                        res = opnd1 / opnd2
                    opnd.push(res)
                    theta1 = optr.get_top()
            if theta1 == '#' or theta2 == '#':
                num = opnd.pop()
                if not opnd.empty():
                    raise Exception('操作数过多')
                opnd.push(num)
    res = opnd.pop()
    return res


if __name__ == '__main__':
    print(calc_infix('5 -  6 * ( 1 +  2 ) - 4'))