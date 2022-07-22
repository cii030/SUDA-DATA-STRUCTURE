class ArrayStack:
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


def prefix(lst: list):
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    operator = {'+', '-', '*', '/'}
    for i in lst:
        if i not in operator:
            if type(eval(i)) == int:
                stack1.push(int(i))
            elif type(eval(i)) == float:
                stack1.push(float(i))
        else:
            stack1.push(i)
    while not stack1.empty():
        item = stack1.pop()
        if item not in operator:
            stack2.push(item)
        else:
            opnd1 = stack2.pop()
            opnd2 = stack2.pop()
            res = 0
            if opnd1 is None or opnd2 is None:
                raise Exception('error')
            if item == '+':
                res = opnd1 + opnd2
            elif item == '-':
                res = opnd1 - opnd2
            elif item == '*':
                res = opnd1 * opnd2
            elif item == '/':
                res = opnd1 / opnd2
            stack2.push(res)
    output = stack2.pop()
    if stack1.empty() and not stack2.empty():
        raise Exception('error')
    return output


if __name__ == '__main__':
    plst = input().split()
    try:
        print(prefix(plst))
    except:
        print("illegal expression")
