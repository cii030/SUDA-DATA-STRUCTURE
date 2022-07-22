import time
import random
import matplotlib.pyplot as plt


def generateString(length):
    res = ''
    base = 'abcdefghigklmnopqrstuvwxyz'
    for i in range(length):
        index = random.randint(0, len(base) - 1)
        res += base[index]
    return res


def isAnagram1(s1, s2):
    lst1 = [i for i in s1]
    lst2 = [i for i in s2]
    lst1.sort()
    lst2.sort()
    return lst1 == lst2


def isAnagram2(s1, s2):
    dic1 = {}
    dic2 = {}
    for i in s1:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] += 1
    for i in s2:
        if i not in dic2:
            dic2[i] = 1
        else:
            dic2[i] += 1
    return dic1 == dic2


def isAnagram3(s1, s2):
    lst2 = [i for i in s2]
    n1 = 0
    res = True
    while n1 < len(s1) and res:
        n2 = 0
        ch = s1[n1]
        found = False
        while not found and n2 < len(lst2):
            if ch == lst2[n2]:
                found = True
            else:
                n2 += 1
        if found:
            lst2[n2] = 0
        else:
            res = False
        n1 += 1
    return res


def compare():
    length = []
    time1 = []
    time2 = []
    time3 = []
    for i in range(1, 500, 10):
        length.append(i)
        s1 = generateString(i)
        s2 = generateString(i)
        start1 = time.perf_counter()
        isAnagram1(s1, s2)
        end1 = time.perf_counter()
        time1.append(end1 - start1)
        start2 = time.perf_counter()
        isAnagram2(s1, s2)
        end2 = time.perf_counter()
        time2.append(end2 - start2)
        start3 = time.perf_counter()
        isAnagram3(s1, s2)
        end3 = time.perf_counter()
        time3.append(end3 - start3)
    plt.xlabel('length')
    plt.ylabel('running time')
    plt.scatter(length, time1, label='way1')
    plt.scatter(length, time2, label='way2')
    plt.scatter(length, time3, label='way3')
    plt.legend()
    plt.show()


compare()
