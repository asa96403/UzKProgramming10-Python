class Node:
    #color: red: 1, black 0
    def __init__(self, value, parent=None, color=1, right=None, left=None) :
        self.value = value
        self.right=right
        self.left=left
        self.parent=parent
        self.color=color
    
    def add(self, val, nil):
        if val>self.value:
            if self.right is nil:
                self.right = Node(val, self, left=nil, right=nil)
                return self.right
            else :
                newNode = self.right.add(val, nil)
        else :
            if self.left is nil:
                self.left=Node(val, self, left=nil, right=nil)
                return self.left
            else :
                newNode = self.left.add(val, nil)
                return newNode

    def search(self, val):
        if self.right == None and self.left==None:
            return None
        elif self.value == val :
            return self
        elif self.value> val :
            self.right.search(val)
        else :
            self.left.search(val)

    def inOrderTreeWalk(self, nil):
        if self.left is not nil:
            self.left.inOrderTreeWalk(nil)
        print(f"{str(self.value)}: color: {str(self.color)}")
        if self.right is not nil:
            self.right.inOrderTreeWalk(nil)

#GETTERS
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def getParent(self):
        return self.parent
    
    def getColor(self):
        return self.color
    
    def getValue(self):
        return self.value
    
#SETTERS
    def setRight(self, right):
        if isinstance(right, Node):
            self.right = right
    
    def setLeft(self, left):
        if isinstance(left, Node):
            self.left = left
    
    def setParent(self, parent):
        if isinstance(parent, Node):
            self.parent = parent
    
    def setColor(self, color):
        if isinstance(color, int) and (color==0 or color ==1):
            self.color = color
    
    def getValue(self, val):
        if isinstance(val, int) :
            self.value = val