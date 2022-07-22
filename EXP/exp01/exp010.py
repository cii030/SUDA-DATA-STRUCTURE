def change(price, pay):
    if price > pay:
        return 'You need more money!'
    else:
        lst = [0.1, 0.5, 1, 5, 10, 20, 50, 100]
        left = pay - price
        lst.append(left)
        lst.sort()
        dic = dict()
        while left > 0.1:
            index = lst.index(left) - 1
            n = left // lst[index]
            dic[str(lst[index])] = str(int(n))
            left = left % lst[index]
            lst.pop(index + 1)
            lst.append(left)
            lst.sort()
        res = '应找零钱 '
        for key, item in dic.items():
            if float(key) > 1:
                res += f'{key}元纸币{item}张 '
            else:
                res += f'{key}元硬币{item}枚 '

        return res


print(change(10, 29))
print(change(10, 51.6))
print(change(10, 5))
