def is_decrease(m: int) -> int:
    n = str(m)
    lst = []
    for i in n:
        lst.append(int(i))
    lst2 = lst[:]
    lst2.sort(reverse=True)
    if lst == lst2:
        return 1
    else:
        return 0


n = int(input())
print(is_decrease(n))


