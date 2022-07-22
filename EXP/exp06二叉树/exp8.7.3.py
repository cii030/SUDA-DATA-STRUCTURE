from heap import BinHeap
import copy


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
            right_node = forest.del_min()
            new_node = HuffmanNode()
            new_node.weight = left_node.weight + right_node.weight
            new_node.left = left_node
            new_node.right = right_node
            left_node.parent = new_node
            right_node.parent = new_node
            forest.insert(new_node)
        self._root = forest.del_min()

    def create_huffman_encoding(self, leaf):
        """用字典储存各个字符的编码"""
        res = {}
        for i in range(len(leaf)):
            p = leaf.del_min()
            data = p.data
            t_code = []
            while p != self._root:
                if p.parent.left == p:
                    t_code.append('0')
                else:
                    t_code.append('1')
                p = p.parent
            t_code.reverse()
            huffman_encodeing = ''.join(i for i in t_code)
            res[data] = huffman_encodeing
        return res

    def huffman_decoding(self, x):
        """解码哈夫曼编码"""
        decoding = ''
        p = self._root
        for i in x:
            if p.data == '#':
                if i == '0':
                    p = p.left
                elif i == '1':
                    p = p.right
            if p.data != '#':
                decoding += p.data
                p = self._root
        return decoding


def create_data_and_weights(x):
    """生成各字符的频率"""
    data_and_weights = {}
    for i in x:
        if i not in data_and_weights:
            data_and_weights[i] = 1
        else:
            data_and_weights[i] += 1
    return data_and_weights


def create_leaf_nodes(data_and_weights):
    """创建leaf_nodes堆，存储初始森林中所有叶结点的指针"""
    leaf_nodes = BinHeap()
    for key, value in data_and_weights.items():
        new_node = HuffmanNode()
        new_node.data = key
        new_node.weight = value
        leaf_nodes.insert(new_node)
    return leaf_nodes


if __name__ == '__main__':
    x = input(':')
    data_and_weights = create_data_and_weights(x)
    print('各字符频率：', data_and_weights)
    huffman = HuffmanTree()
    leaf_nodes = create_leaf_nodes(data_and_weights)
    forest = copy.copy(leaf_nodes)
    huffman.create(forest)
    huffman_encoding = huffman.create_huffman_encoding(leaf_nodes)
    print('各字符的哈夫曼编码：', huffman_encoding)
    res = ''
    for i in x:
        res += huffman_encoding[i]
    print('压缩后为：', res)
    print('解码后为：', huffman.huffman_decoding(res))
