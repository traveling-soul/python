class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        # 当前节点的值
        self.elem = elem
        # 左子树
        self.lchild = lchild
        # 右子树
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self, root=None):
        # 根节点
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行遍历
            while queue:
                # 弹出列表的第一个元素
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，压栈继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.preorder(root.lchild)
        print(root.elem)
        self.preorder(root.rchild)

    def postorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        print(root.elem)

    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)
        return queue


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    # 先序遍历
    # tree.preorder(tree.root)
    # 中序遍历
    # tree.inorder(tree.root)
    # 后序遍历
    # tree.postorder(tree.root)
    # 广度优先
    tree.breadth_travel(tree.root)


