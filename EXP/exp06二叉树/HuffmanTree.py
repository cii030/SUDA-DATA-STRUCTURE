class HuffmanNode:
    def __init__(self):
        self.data = '#'
        self.weight = -1
        self.parent = None
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

class HuffmanTree:
    def __init__(self):
        self._root = None

    def create(self, forest):
        """哈夫曼树的创建算法，forest为存放初始森林中各叶结点的堆，
        注意创建结束后forest为空堆，并会影响实参堆"""
        while len(forest) > 1:
            left_node = forest.del_min()  # 连续删除forest当中两个权值最小的根结点
            right_node = forest.del_min
            new_node = HuffmanNode()
            new_node.left = left_node
            new_node.right = right_node
            left_node.parent = new_node
            right_node.parent = new_node
            forest.insert(new_node)
        self._root = forest.del_min()

    def huffman_encoding(self, leaf):
        print('各字符的哈夫曼编码如下：')
        for i in range(len(leaf)):
            p = leaf.del_min()
            print(p.data, end=':')
            t_code = []
            while p != self._root:
                if p.parent.left == p:
                    t_code.append('0')
                else:
                    t_code.append('1')
                p = p.parent
            t_code.reverse()
            print(''.join(i for i in t_code))
