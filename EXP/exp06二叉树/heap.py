from HuffmanTree import HuffmanNode


class BinHeap:
    def __init__(self):
        self.data = []

    def __copy__(self):
        new_heap = BinHeap()
        new_heap.data = self.data[::]
        return new_heap

    def __len__(self):
        return len(self.data)

    def sift_up(self, i):
        """从i号位置开始向上筛选"""
        #  由于列表中元素的下标从0开始编号，i号元素的父节点编号为(i-1)//2
        while (i - 1) // 2 >= 0:
            if self.data[i] < self.data[(i - 1) // 2]:
                self.data[(i - 1) // 2], self.data[i] = self.data[i], self.data[(i - 1) // 2]
            i = (i - 1) // 2  # i更新为其父结点编号

    def insert(self, x):
        self.data.append(x)
        self.sift_up(len(self.data) - 1)

    def sift_down(self, i, end):
        """对当前堆从i号位置开始向下筛选，筛选的结束位置为end"""
        j = 2 * i + 1  # j为i号结点的左孩子编号
        x = self.data[i]  # 当时堆顶的值
        while j <= end:
            if j < end and self.data[j + 1] < self.data[j]:
                j = j + 1  # j为i号结点更小孩子的编号
            if x <= self.data[j]:
                break  # x应在i号位置
            else:
                #  更小的孩子j号应该与父结点i号交换，但由于j号位置不一定是x的最终位置，在此做单方向赋值，只将该孩子提升到i号位置
                self.data[i] = self.data[j]
                i = j
                j = 2 * j + 1
        self.data[i] = x

    def del_min(self):
        min_val = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]  # 将最后一个叶子的值替换到堆顶
        self.data.pop()  # 删除列表中最后一个叶子
        if len(self.data) > 0:  # 如果堆中还有元素
            self.sift_down(0, len(self.data) - 1)  # 从0号位置开始向下筛选
        return min_val


def create_leaf_nodes(data_and_weights):
    """创建leaf_nodes堆，存储初始森林中所有叶结点的指针"""
    leaf_nodes = BinHeap()
    for key, value in data_and_weights.items():
        new_node = HuffmanNode()
        new_node.data = key
        new_node.weight = value
        leaf_nodes.insert(new_node)
    return leaf_nodes

if __name__ == "__main__":
    heap = BinHeap()
    heap.insert(3)
    heap.insert(4)
    heap.del_min()