import time
import matplotlib.pyplot as plt


def way1(n):
    lst = [0]*n


def way2(n):
    lst = list(range(n))


def way3(n):
    lst = []
    for i in range(n):
        lst.append(i)


def way4(n):
    lst = [i for i in range(n)]

def compare():
    length = []
    time1 = []
    time2 = []
    time3 = []
    time4 = []
    for i in range(1, 500, 10):
        length.append(i)
        start1 = time.perf_counter()
        way1(i)
        end1 = time.perf_counter()
        time1.append(end1 - start1)
        start2 = time.perf_counter()
        way2(i)
        end2 = time.perf_counter()
        time2.append(end2 - start2)
        start3 = time.perf_counter()
        way3(i)
        end3 = time.perf_counter()
        time3.append(end3 - start3)
        start4 = time.perf_counter()
        way4(i)
        end4 = time.perf_counter()
        time4.append(end4 - start4)
    plt.xlabel('length')
    plt.ylabel('running time')
    plt.scatter(length, time1, label='way1')
    plt.scatter(length, time2, label='way2')
    plt.scatter(length, time3, label='way3')
    plt.scatter(length, time4, label='way4')
    plt.legend()
    plt.show()


compare()