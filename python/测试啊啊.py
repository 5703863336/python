class Node():
    def __init__(self,values):
        self.values = values
        self.rchild = None
        self.lchild = None

class Tree():
    def __init__(self):
        self.root = None
    def add(self,values):
        node = Node(values)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]


        while queue:
            c_node = queue.pop(0)
            if c_node.lchild is None:
                c_node.lchild = node
                return
            else:
                queue.append(c_node.lchild)
            if c_node.rchild is None:
                c_node.rchild = node
                return
            else:
                queue.append(c_node.rchild)
    def with_drive(self):
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            c_node = queue.pop(0)
            print(c_node.values)
            if c_node.lchild is not None:
                queue.append(c_node.lchild)
            if c_node.rchild is not None:
                queue.append((c_node.rchild))
    def xianxu(self,node):
        if node ==None:
            return
        print(node.values)
        self.xianxu(node.lchild)
        self.xianxu(node.rchild)
    def zhongxu(self,node):
        if node == None:
            return
        self.zhongxu(node.lchild)
        print(node.values)
        self.zhongxu(node.rchild)
    def houxu(self,node):
        if node == None:
            return
        self.houxu(node.lchild)
        self.houxu(node.rchild)
        print(node.values)



if __name__ =="__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.houxu(tree.root)
