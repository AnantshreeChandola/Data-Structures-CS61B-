import math
class Traversal:
    size = 0
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None

    def Insert(self, key):
            if (self == None or self.val == None):
                Traversal.size += 1
                return Traversal(key)
            elif (self.val > key):
                self.left = Traversal.Insert(self.left, key)
            else:
                self.right = Traversal.Insert(self.right, key)
            return self

    def Height(self):
        if self == None:
            return 0
        else:
            lh = Traversal.Height(self.left)
            rh = Traversal.Height(self.right)

            if lh > rh:
                return lh+1
            else:
                return rh+1


    ''' RECURSIVE LEVELORDER [O(N^2)] 
    def Printlevelorder(self, level):
            if self == None:
                return None
            elif level == 1:
                print(self.val, end = " ")
            else:
                Traversal.Printlevelorder(self.left, level-1)
                Traversal.Printlevelorder(self.right, level-1)
    def Levelordertraversal(self):
            height = self.Height()
            for i in range(1, height+1):
                Traversal.Printlevelorder(self, i)'''

    def Levelordertraversal(self):
            if self == None:
                return
            queue = [self]
            while queue:
                s = queue.pop(0)
                print(s.val)
                if s.left:
                    queue.append(s.left)
                if s.right:
                    queue.append(s.right)
    
    def Preorder(self):
        if self:
            print(self.val, end=" ")
            Traversal.Preorder(self.left)
            Traversal.Preorder(self.right)

    def Inorder(self):
        if self:
            Traversal.Inorder(self.left)
            print(self.val, end=" ")
            Traversal.Inorder(self.right)

    def Postorder(self):
        if self:
            Traversal.Postorder(self.left)
            Traversal.Postorder(self.right)
            print(self.val, end=" ")
        
root = Traversal()
root = root.Insert(10)
root = root.Insert(9)
root = root.Insert(11)
root = root.Insert(8)
root = root.Insert(12)
root.Levelordertraversal()
root.Preorder()
root.Inorder()
root.Postorder()
