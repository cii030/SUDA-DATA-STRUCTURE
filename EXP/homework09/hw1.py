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

    def preorder(self):
        """先序遍历接口方法"""
        self.recursive_preorder(self._root)
        print()

    def recursive_preorder(self, sub_root):
        """先序遍历递归算法"""
        if sub_root:
            print(sub_root.data, end=" ")
            self.recursive_preorder(sub_root.left)
            self.recursive_preorder(sub_root.right)

    def remove_degree1(self):
        self._root = self.rec_remove_degree1(self._root)

    def rec_remove_degree1(self, sub_root):
        if sub_root is None:
            return None
        if not sub_root.left and not sub_root.right:
            return sub_root
        if sub_root.left and sub_root.right:
            sub_root.left = self.rec_remove_degree1(sub_root.left)
            sub_root.right = self.rec_remove_degree1(sub_root.right)
            return sub_root
        else:
            node = sub_root.left or sub_root.right
            if not node.left and not node.right:
                sub_root = node
                return sub_root
            else:
                node = self.rec_remove_degree1(node)
                sub_root = node
                return sub_root

if __name__ == "__main__":
    bt1 = BinaryTree()
    lst = input().split()
    bt1.create1(lst)
    bt1.remove_degree1()
    bt1.preorder()