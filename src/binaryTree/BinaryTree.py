from Node import Node

"""Implementierung eines Rot-Schwraz Baums wie in der Vorlesung Algorithmen und Datenstrukturen behandelt"""
class BinaryTree:
    def __init__(self):
        self.root= None
        self.nil = Node(None, color=0)
    
    def add(self, val, nil=None):
        nil = self.nil
        if self.root is None:
            self.root = Node(val, nil, 0, nil, nil)
        else :
            newNode = self.root.add(val, nil)
            self.einfuegenFix(newNode, nil)

    def displayTreeInOrder(self) :
        print("Tree displayed in the oreder of an in-order-tree-walk")
        if self.root is not None:
            self.root.inOrderTreeWalk(self.nil)
        else :
            print("Tree is empty")

    # x ist der Startknoten der Suche
    def minimumSuche(self, x):
        while x.getLeft() is not self.nil:
            x=x.getLeft()
        return x

    # x ist der Knoten, dessen Nachfolger gefunden werden soll
    def findeNachbarn(self, x):
        if x.getRight() is not self.nil:
            return self.minimumSuche(x.getRight())
        else :
            y = x.getParent()
            while y is not self.nil and x is y.getRight() :
                x=y
                y=y.getParent()
            return y

    def search(self, val):
        return self.root.search(val, self.nil)

#x ist der Knoten,,um den rotiert werden soll
    def linksrotation(self, x, nil):
        y=x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() is not nil:
            y.getLeft().setParent(x)
        y.setParent(x.getParent())
        if x.getParent() is nil:
            self.root=y
        elif x.getParent().getLeft() is x:
             x.getParent().setLeft(y)
        else :
            x.getParent().setRight(y)
        y.setLeft(x)
        x.setParent(y) 

#gleich wie linksrotation nur Spiegelverkehrt
    def rechtsrotation(self, y, nil):
        x=y.getLeft()
        y.setLeft(x.getRight())
        if x.getRight() is not nil:
            x.getRight().setParent(y)
        x.setParent(y.getParent())
        if y.getParent() is nil:
            self.root=x
        elif y.getParent().getLeft is y:
            y.getParent().setLeft(x)
        else :
            y.getParent().setRight(x)
        x.setRight(y)
        y.setParent(x) 

#balanciert den Suchbaum nach dem Einfügen eines Knotens nach den rot-schwarz Eigenschaften
# rot: 1, schwarz: 0
    def einfuegenFix(self, z, nil):
        while z.getParent().getColor() == 1:
            if z.getParent() is z.getParent().getParent().getLeft() :
                y = z.getParent().getParent().getRight() # Setzen des Onkelknotens
                if y.getColor() == 1 : #Fall 2
                    z.getParent().setColor(0)
                    y.setColor(0)
                    z.getParent().getParent().setColor(1)
                    z = z.getParent().getParent()
                elif z is z.getParent().getRight():
                    z = z.getParent()
                    self.linksrotation(z, nil)
                    z.getParent().setColor(0)
                    z.getParent().getParent().setColor(1)
                    self.rechtsrotation(z.getParent().getParent(), nil)
            #symmetrischerFall
            else :
                y = z.getParent().getParent().getLeft() # Setzen des Onkelknotens
                if y.getColor()==1: #Fall 2
                    z.getParent().setColor(0)
                    y.setColor(0)
                    z.getParent().getParent().setColor(1)
                    z=z.getParent().getParent()
                elif z is z.getParent().getLeft:
                    z = z.getParent()
                    self.rechtsrotation(z, nil)
                    z.getParent().setColor(0)
                    z.getParent().getParent().setColor(1)
                    self.linksrotation(z.getParent().getParent(), nil)
            self.root.setColor(0)

