class BinaryNode:
    def __init__(self, data="#", left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def create1(self, pre):
        self._root = self.recursive_create1(pre)

    def recursive_create1(self, preorder):
        if len(preorder) == 0:
            raise ValueError("不合法的带#先序序列")
        data = preorder.pop(0)  # 删除列表首元素，并赋值给data
        if data == '#':  # 如果data为“#”
            return None  # 生成空二叉树
        else:
            new_root = BinaryNode(data)  # 以data值生成结点new_root
            # 以删除了首元素的新preorder列表生成new_root的左子树
            new_root.left = self.recursive_create1(preorder)
            # 以删除了首元素以及new_root左子树对应元素的新preorder列表
            # 生成new_root的右子树
            new_root.right = self.recursive_create1(preorder)
            return new_root

    def rec_find_parents(self, x, sub_root):
        if not sub_root:
            return None
        if not sub_root.left and not sub_root.right:
            return None
        if sub_root.left and sub_root.right:
            if sub_root.left.data == x or sub_root.right.data == x:
                return sub_root.data
            return self.rec_find_parents(x, sub_root.left) or self.rec_find_parents(x, sub_root.right)
        else:
            if sub_root.left:
                if sub_root.left.data == x:
                    return sub_root.data
                return self.rec_find_parents(x, sub_root.left)
            else:
                if sub_root.right.data == x:
                    return sub_root.data
                return self.rec_find_parents(x, sub_root.right)

    def find_parents(self, x):
        return self.rec_find_parents(x, self._root)


if __name__ == "__main__":
    bt1 = BinaryTree()
    lst = input().split()
    bt1.create1(lst)
    n = input()
    print(bt1.find_parents(n))
