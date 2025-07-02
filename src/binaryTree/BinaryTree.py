from Node import Node

"""Implementierung eines Rot-Schwraz Baums wie in der Vorlesung Algorithmen und Datenstrukturen behandelt"""
class BinaryTree:
    def __init__(self):
        self.root= None
    
    def add(self, val):
        if self.root == None:
            root = Node(val)
        else :
            root.add(val)


#x ist der Knoten,,um den rotiert werden soll
    def linksrotation(self, x):
        y=x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() is not None:
            y.getLeft().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is None:
            self.root=y
        elif x.getParent().getLeft == x:
            x.getParent().setLeft(y)
        else :
            x.getParent().setRight(y)
        y.setLeft(x)
        x.setParent(y) 

#gleich wie linksrotation nur Spiegelverkehrt
    def rechtsrotation(self, y):
        x=y.getLeft()
        y.setLeft(x.getRight())
        if x.getRight() is not None:
            x.getRight().setParent(y)
        x.setParent(y.getParent())
        if y.getParent() is None:
            self.root=x
        elif y.getParent().getLeft == y:
            y.getParent().setLeft(x)
        else :
            y.getParent().setRight(x)
        x.setRight(y)
        y.setParent(x) 

