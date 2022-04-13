class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self, value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        if self.left:
            self.left.preorder_traversal()
        print(self.value)
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True



tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19, {"data": "Hello World"})
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

tree.inorder_traversal()
print(tree.find(2))
print(tree.find(19).content['data'])

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
