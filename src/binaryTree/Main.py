from BinaryTree import BinaryTree
from Node import Node

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(5)
    tree.displayTreeInOrder()
    tree.add(4)
    tree.displayTreeInOrder()
    tree.add(8)
    tree.displayTreeInOrder()
    tree.add(1)
    tree.displayTreeInOrder()
  #  tree.rechtsrotation(tree.root, tree.nil)
   # print(str(tree.root.left.value))
   # print(str(tree.root.value))
   # print(str(tree.root.right.value))
  #  print(str(tree.root.right.right.value))
    print(tree.search(4).value)
    print(tree.findeNachbarn(tree.search(4)).value)
    tree.add(2)
    tree.displayTreeInOrder()