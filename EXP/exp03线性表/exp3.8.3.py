from Node import Node


class consumption:
    def __init__(self, date, project, bill):  # 一项支出的日期，项目，价格
        bill = int(bill)
        self.date = date
        self.project = project
        self.bill = bill

    def __str__(self):
        res = self.date + ' ' + self.project + ' ' + str(self.bill)
        return res

    def get_date(self):
        return self.date

    def get_project(self):
        return self.project

    def get_bill(self):
        return self.bill


class financial_management:  # 链表思想
    def __init__(self):
        self._head = Node(None)

    def append(self, item):  # 前插法 降低插入的复杂度
        new_node = Node(item)
        new_node.next = self._head.next
        self._head.next = new_node

    def traverse(self):
        """输出所有项目"""
        p = self._head.next
        while p is not None:
            print(p.entry)
            p = p.next

    def get_min(self):
        """获取最小消费"""
        p = self._head.next
        min_bill = p.entry.get_bill()
        min_project = p.entry
        while p is not None:
            item = p.entry
            if min_bill >= item.get_bill():
                min_bill = item.get_bill()
                min_project = p.entry
            p = p.next
        return min_project

    def get_max(self):
        """获取最大消费"""
        p = self._head.next
        max_bill = p.entry.get_bill()
        max_project = p.entry
        while p is not None:
            item = p.entry
            if max_bill <= item.get_bill():
                max_bill = item.get_bill()
                max_project = p.entry
            p = p.next
        return max_project

    def get_average(self):
        """获取平均消费"""
        p = self._head.next
        total = 0
        count = 0
        while p is not None:
            total += p.entry.get_bill()
            count += 1
            p = p.next
        res = total / count
        return res

    def find_day(self, date):
        """按照日期找出某一天的所有花费"""
        p = self._head.next
        total = 0
        while p is not None:
            if p.entry.get_date() == date:
                print(p.entry)
                total += p.entry.get_bill()
            p = p.next
        print(f'总花费{total}')

    def find_day_project(self, date, project):
        """按照日期和支出项目找出该项目花费"""
        p = self._head.next
        while p is not None:
            if p.entry.get_date() == date:
                if p.entry.get_project() == project:
                    return p.entry.get_bill()
            p = p.next
        return None

    def find_totalbill(self, project):
        """按照项目找出该支出项目的所有花费"""
        p = self._head.next
        total = 0
        while p:
            if p.entry.get_project() == project:
                total += p.entry.get_bill()
            p = p.next
        return total

    def decrease_output(self):
        """按照支出项花费递减的顺序输出每一项的对应总花费"""
        dic = {}
        p = self._head.next
        while p:
            if p.entry.get_project() not in dic:
                dic[p.entry.get_project()] = p.entry.get_bill()
            else:
                dic[p.entry.get_project()] += p.entry.get_bill()
            p = p.next
        res = list(dic.items())
        res.sort(key=lambda i: i[1], reverse=True)
        for i in res:
            print(f'{i[0]}花费了{i[1]}')


def get_consumption():  # 读取文件，创建链表
    f = open('index.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    lst = []
    financial_lst = financial_management()
    for line in lines:
        lst.append(line.strip('\n'))
    for i in lst:
        lst2 = i.split()
        pro = consumption(lst2[0], lst2[1], lst2[2])
        financial_lst.append(pro)
    return financial_lst


if __name__ == '__main__':
    pass
