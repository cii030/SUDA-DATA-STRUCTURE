import time
import matplotlib.pyplot as plt
import random


def index_time():
    dic = {}
    for i in range(100, 100000, 1000):
        x = list(range(i))
        index = random.randint(1, i)
        start = time.perf_counter()
        num = x[index]
        end = time.perf_counter()
        t = end - start
        dic[i] = t
    plt.xlabel('length')
    plt.ylabel('running time')
    x = [i for i in dic.keys()]
    y = [i for i in dic.values()]
    plt.scatter(x, y, label='index')
    plt.legend()
    plt.show()


def dic_time():
    dic1 = {}
    dic2 = {}
    for i in range(10, 1000000, 10000):
        test_dic = {j: j for j in range(i)}
        index = random.randint(1, i)
        start1 = time.perf_counter()
        num = test_dic[index]
        end1 = time.perf_counter()
        t1 = end1 - start1
        dic1[i] = t1
        start2 = time.perf_counter()
        test_dic[i] = 1
        end2 = time.perf_counter()
        t2 = end2 - start2
        dic2[i] = t2
    plt.xlabel('length')
    plt.ylabel('running time')
    x1 = [i for i in dic1.keys()]
    y1 = [i for i in dic1.values()]
    x2 = [i for i in dic2.keys()]
    y2 = [i for i in dic2.values()]
    plt.scatter(x1, y1, label='read')
    plt.scatter(x2, y2, label='write', marker='*')
    plt.legend()
    plt.show()


def sort_time():
    dic1 = {}
    dic2 = {}
    for i in range(10000, 1000001, 10000):
        x1 = [random.randint(1, i) for j in range(i)]
        start = time.perf_counter()
        x1.sort()
        end = time.perf_counter()
        t = end - start
        dic1[i] = t
        x2 = [j for j in range(i)]
        start2 = time.perf_counter()
        x2.sort()
        end2 = time.perf_counter()
        t2 = end2 - start2
        dic2[i] = t2
    plt.xlabel('length')
    plt.ylabel('running time')
    x = [i for i in dic1.keys()]
    y1 = [i for i in dic1.values()]
    y2 = [i for i in dic2.values()]
    plt.scatter(x, y1, label='random list')
    plt.scatter(x, y2, label='incremental list')
    plt.legend()
    plt.show()

dic_time()
