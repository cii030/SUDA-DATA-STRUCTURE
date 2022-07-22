from LinkedStack import LinkedStack
from CircularQueue import CircularQueue


class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def build_tree_string(self, root, delimiter='-'):
        if root is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        node_repr = str(root.data)
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = self.build_tree_string(root.left, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = self.build_tree_string(root.right, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0
        line1.append(node_repr)
        line2.append(' ' * new_root_width)
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + r'\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def print_tree(self):
        lines = self.build_tree_string(self._root)[0]
        a = '\n' + '\n'.join((line.rstrip() for line in lines))
        print(a)

    def recursive_create2(self, preorder, inorder):
        """以二叉树的先序和中序序列创建二叉树"""
        if len(preorder) == 0:
            return None
        root_char = preorder[0]  # root_char为根结点值
        root_in = inorder.find(root_char)  # 在中序序列中定位根的位置
        if root_in == -1:
            raise ValueError('不是合法的序列')
        left_in = inorder[:root_in]  # 获得左子树的中序序列
        right_in = inorder[root_in + 1:]  # 获得右子树的中序序列
        left_pre = preorder[1:root_in + 1]  # 获得左子树的先序序列
        right_pre = preorder[root_in + 1:]  # 获得右子树的先序序列
        new_root = BinaryNode(root_char)
        new_root.left = self.recursive_create2(left_pre, left_in)
        new_root.right = self.recursive_create2(right_pre, right_in)
        return new_root

    def create2(self, preorder, inorder):
        if len(preorder) != len(inorder):
            raise ValueError('不是合法的序列')
        self._root = self.recursive_create2(preorder, inorder)

    def recursive_preorder(self, sub_root):
        """先序遍历递归算法"""
        if sub_root:
            print(sub_root.data, end=' ')
            self.recursive_preorder(sub_root.left)
            self.recursive_preorder(sub_root.right)

    def preorder0(self):
        """先序遍历接口方法"""
        self.recursive_preorder(self._root)

    def recursive_inorder(self, sub_root):
        """中序遍历递归算法"""
        if sub_root:
            self.recursive_inorder(sub_root.left)
            print(sub_root.data, end=' ')
            self.recursive_inorder(sub_root.right)

    def inorder0(self):
        """中序遍历接口方法"""
        self.recursive_inorder(self._root)

    def recursive_postorder(self, sub_root):
        """后序遍历递归算法"""
        if sub_root:
            self.recursive_postorder(sub_root.left)
            self.recursive_postorder(sub_root.right)
            print(sub_root.data, end=' ')

    def postorder0(self):
        """后序遍历接口方法"""
        self.recursive_postorder(self._root)

    def preorder1(self):
        """先序遍历的非递归实现1:中序遍历的修改"""
        s = LinkedStack()
        p = self._root
        while not s.empty() or p:
            if p:
                print(p.data, end=' ')
                s.push(p)
                p = p.left
            else:
                p = s.pop()
                p = p.right

    def preorder2(self):
        """仅入栈结点的非空右孩子"""
        p = self._root
        s = LinkedStack()
        while not s.empty() or p:
            if p:
                print(p.data, end=' ')
                if p.right:
                    s.push(p.right)
                p = p.left
            else:
                p = s.pop()

    def inorder(self):
        """中序遍历的非递归实现"""
        s = LinkedStack()
        p = self._root
        while not s.empty() or p:
            while p:
                s.push(p)
                p = p.left
            if not s.empty():
                p = s.pop()
                print(p.data, end=' ')
                p = p.right

    def postorder(self):
        """后序遍历的非递归实现"""
        p = self._root
        s = LinkedStack()
        q = None
        while not s.empty() or p:
            while p:
                s.push(p)
                p = p.left
            while not s.empty():
                p = s.get_top()
                if not p.right or p.right == q:
                    p = s.pop()
                    print(p.data, end=' ')
                    q = p
                    if p == self._root:
                        return
                else:
                    p = p.right
                    break

    def level_traversal(self):
        """层次遍历算法"""
        if self._root is None:
            return
        q = CircularQueue()
        q.append(self._root)
        while not q.empty():
            p = q.serve()
            print(p.data, end=' ')
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

    def recursive_depth(self, sub_root):
        """求二叉树深度"""
        if not sub_root:
            return 0
        else:
            left_height = self.recursive_depth(sub_root.left)
            right_height = self.recursive_depth(sub_root.right)
            return max(left_height, right_height) + 1

    def depth(self):
        return self.recursive_depth(self._root)

    def width(self):
        """求二叉树宽度"""
        if self._root is None:
            return 0
        q = CircularQueue()
        cur_wid = 1
        max_wid = 1
        q.append(self._root)
        while not q.empty():
            n = cur_wid
            for i in range(n):
                temp = q.serve()
                cur_wid -= 1
                if temp.left:
                    q.append(temp.left)
                    cur_wid += 1
                if temp.right:
                    q.append(temp.right)
                    cur_wid += 1
            max_wid = max(max_wid, cur_wid)
        return max_wid

    def recursive_degree0_size(self, sub_root):
        """统计二叉树上度为0的结点数"""
        if not sub_root:
            return 0
        if not sub_root.left and not sub_root.right:
            return 1
        else:
            return self.recursive_degree0_size(sub_root.left) + self.recursive_degree0_size(sub_root.right)

    def degree0_size(self):
        return self.recursive_degree0_size(self._root)

    def recursive_degree1_size(self, sub_root):
        """统计二叉树上度为1的结点数"""
        if not sub_root:
            return 0
        if not sub_root.left and not sub_root.right:
            return 0
        if sub_root.left and sub_root.right:
            return self.recursive_degree1_size(sub_root.left) + self.recursive_degree1_size(sub_root.right)
        else:
            return 1 + self.recursive_degree1_size(sub_root.left) + self.recursive_degree1_size(sub_root.right)

    def degree1_size(self):
        return self.recursive_degree1_size(self._root)

    def recursive_degree2_size(self, sub_root):
        """统计二叉树上度为2的结点数"""
        if not sub_root:
            return 0
        if not sub_root.left and not sub_root.right:
            return 0
        if sub_root.left and sub_root.right:
            return 1 + self.recursive_degree2_size(sub_root.left) + self.recursive_degree2_size(sub_root.right)
        else:
            return self.recursive_degree2_size(sub_root.left) + self.recursive_degree2_size(sub_root.right)

    def degree2_size(self):
        return self.recursive_degree2_size(self._root)

    def rec_find_parents(self, x, sub_root):
        """查找值为x的双亲"""
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

    def find_sibling(self, x):
        """查找值x的兄弟"""
        q = CircularQueue()
        cur_wid = 1
        q.append(self._root)
        lst = []
        while not q.empty():
            lst.clear()
            n = cur_wid
            for i in range(n):
                temp = q.serve()
                lst.append(temp.data)
                cur_wid -= 1
                if temp.left:
                    q.append(temp.left)
                    cur_wid += 1
                if temp.right:
                    q.append(temp.right)
                    cur_wid += 1
            if x in lst:
                res = ' '.join(i for i in lst if i != x)
                return res
        return None

    def insert_lower(self, x):
        new_node = BinaryNode(x)
        if self._root is None:
            self._root = new_node
            return self._root
        q = CircularQueue()
        q.append(self._root)
        while not q.empty():
            p = q.serve()
            if not p.left:
                p.left = new_node
                return
            else:
                q.append(p.left)
            if not p.right:
                p.right = new_node
                return
            else:
                q.append(p.right)


    def rec_del_child(self, x, sub_root):
        """删除以值为x的结点为根的子树"""
        if not sub_root:
            return None
        if not sub_root.left and not sub_root.right:
            return sub_root
        else:
            if sub_root.data == x:
                sub_root.left = None
                sub_root.right = None
                return sub_root
            else:
                sub_root.left = self.rec_del_child(x, sub_root.left)
                sub_root.right = self.rec_del_child(x, sub_root.right)
                return sub_root

    def del_child(self, x):
        return self.rec_del_child(x, self._root)


if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.create2('ABCDEFGH', 'BDCEAFHG')
    binary_tree.print_tree()
    binary_tree.insert_lower('I')
    print('插入I在最短子树')
    binary_tree.print_tree()
