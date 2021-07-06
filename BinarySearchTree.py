class BinarySearchTree:
    size = 0
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None
    def insert(self, key):
        if (self == None or self.val == None):
            BinarySearchTree.size += 1
            return BinarySearchTree(key)
        else:
            if self.val < key:
                self.right = BinarySearchTree.insert(self.right, key)
            else:
                self.left = BinarySearchTree.insert(self.left, key)
        return self
    def search(self, key):
        if (self == None or self.val == None):
            return None
        elif(self.val == key):
            return True
        elif(self.val < key):
            return BinarySearchTree.search(self.right, key)
        else:
            return BinarySearchTree.search(self.left, key)
    def minvaluenode(self):
        if self == None or self.val == None:
            return None
        elif(self.left == None):
            return self
        else:
            return BinarySearchTree.minvaluenode(self.left)
    def delete(self, key):
        if self == None or self.val == None:
            return None
        elif self.val < key:
            self.right = BinarySearchTree.delete(self.right, key)
        elif self.val > key:
            self.left = BinarySearchTree.delete(self.left, key)
        else:
            if self.left == None:
                temp = self.right
                self = None
                return temp
            elif self.right == None:
                temp = self.left
                self = None
                return temp
            else:
                temp = BinarySearchTree.minvaluenode(self.right)
                self.val = temp.val
                self.right = BinarySearchTree.delete(self.right, temp.val)
        return self
    def preorder(self):
        if self:
            print(self.val)
            BinarySearchTree.preorder(self.left)  
            BinarySearchTree.preorder(self.right)

bst = BinarySearchTree()
bst = bst.insert(2)
bst = bst.insert(8)
bst = bst.insert(3)
bst = bst.insert(4)
bst = bst.insert(0)
bst = bst.insert(1)
bst.preorder()
print(bst.size)
print(bst.search(8))
print(bst.minvaluenode().val)
bst = bst.delete(2)
bst.preorder()