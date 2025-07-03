from Node import Node

"""Implementierung eines Rot-Schwraz Baums wie in der Vorlesung Algorithmen und Datenstrukturen behandelt"""
class BinaryTree:
    def __init__(self):
        self.root= None
    
    def add(self, val):
        if self.root is None:
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
        elif x.getParent().getLeft is x:
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
        elif y.getParent().getLeft is y:
            y.getParent().setLeft(x)
        else :
            y.getParent().setRight(x)
        x.setRight(y)
        y.setParent(x) 

#balanciert den Suchbaum nach dem Einfügen eines Knotens nach den rot-schwarz Eigenschaften
# rot: 1, schwarz: 0
    def einfügenFix(self, z):
        while z.getParent().getColor()==1:
            if z.getParent() is z.getParent().getParent().getLeft() :
                y = z.getParent().getParent().getRight() # Setzen des Onkelknotens
                if y.getColor == 1 : #Fall 2
                    z.getParent().setColor(0)
                    y.setColor(0)
                    z.getParent().getParent().setColor(1)
                    z.getParent().setParent(z)
                elif z is z.getParent().getRight():
                    z = z.getParent()
                    self.linksrotation(z)
                    z.getParent().setColor(0)
                    z.getParent().getParent().setColor(1)
                    self.rechtsrotation(z.getParent().getParent())
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
                    self.rechtsrotation(z)
                    z.getParent().setColor(0)
                    z.getParent().getParent().setColor(1)
                    self.linksrotation(z.getParent().getParent())
            self.root.setColor(0)

