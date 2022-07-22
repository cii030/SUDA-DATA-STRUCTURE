def temDays2(temperatures: list) -> list:
    stack = []
    res = [0 for i in range(len(temperatures))]
    current_day = 0
    for i in temperatures:
        while stack and i > temperatures[stack[-1]]:
            former_day = stack.pop()
            res[former_day] = current_day - former_day
        stack.append(current_day)
        current_day += 1
    return res


if __name__ == '__main__':
    n = input()
    temperatures = list(map(int, n.split()))
    print(temDays2(temperatures))
