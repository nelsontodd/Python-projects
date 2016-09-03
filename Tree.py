class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  def isSimilar (self, pNode):
      for i in range(1,self.getHeight()+1):
          if self.printLevel(i) == pNode.printLevel(i):
              print('Level '+str(i) + ' : '+ self.printLevel(i))

  def printLevel1 (self,current, level,idx,returnStr,lvl = 1):
      if lvl == level:
          returnStr[idx] = current.data
      else:
          temp = current
          if current.lchild != None:
              current = current.lchild
              self.printLevel1(current,level,idx,returnStr,lvl+1)
          if temp.rchild != None:
              currentR = temp.rchild
              idx +=level-(lvl-1)
              self.printLevel1(currentR,level,idx,returnStr,lvl+1)
  def printLevel (self,level, side = ' '):
      returnStr = [None] * 2**self.getHeight()
      if side == 'left':
          current = self.root
          current = current.lchild
      elif side == 'right':
          current = self.root
          current = current.rchild
      else:
          current = self.root
      self.printLevel1(current,level,0,returnStr,1)
      stringy = ''
      for i in range(len(returnStr)):
          if returnStr[i] != None:
              stringy +=str(returnStr[i]) + ' '
      return stringy
  def getHeight (self):
      Lengths = []
      current = self.root
      self.sub_sets(current,1,Lengths)
      return max(Lengths)
  def sub_sets (self, current, idx,Lengths): #Finds all sub sets of the input and adds them to the list if they are a nestedbox
    if (current.lchild == None and current.rchild == None):
        Lengths.append(idx)
    else:
        temp = current
        current = current.lchild
        currentR = temp.rchild
        self.sub_sets (current, idx + 1, Lengths)
        self.sub_sets (currentR, idx + 1, Lengths)

  def numNodes (self):
      leftStr = ''
      rightStr = ''
      i = 1
      while i <= self.getHeight():
          leftStr+= self.printLevel(i,'left')
          rightStr+= self.printLevel(i,'right')
          i+=1
      return 'Left: '+str(len(leftStr.split())) + ' Right: '+str(len(rightStr.split()))
  # search for a node with a key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
	if (val < current.data):
	  current = current.lchild
	else:
	  current = current.rchild
      if (val < parent.data):
        parent.lchild = newNode
      else:
        parent.rchild = newNode

  # in order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lchild)
      return (aNode.data)
      self.inOrder (aNode.rchild)

  # pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)

  # post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lchild)
      self.postOrder (aNode.rchild)
      print (aNode.data)

  # delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # if empty tree
    if (deleteNode == None):
      return False

    # find the delete node
    while ((deleteNode != None) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lchild
	isLeft = True
      else:
        deleteNode = deleteNode.rchild
	isLeft = False

    # if node not found
    if (deleteNode == None):
      return False

    # delete node is a leaf node
    if (deleteNode.lchild == None) and (deleteNode.rchild == None):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lchild = None
      else:
        parent.rchild = None

def main():
    # Create three trees - two are the same and the third is different
    Vals = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    Vals1 = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    Vals2 = [51, 30, 70, 10, 40, 60, 82, 7, 25, 38, 47, 58, 65, 77, 96]
    tree1 = Tree()
    tree2 = Tree()
    tree3 = Tree()
    for i in range(len(Vals)):
        tree1.insert(Vals[i])
        tree2.insert(Vals1[i])
        tree3.insert(Vals2[i])
    # Test your method isSimilar()
    # Print the various levels of two of the trees that are different
    print(tree1.isSimilar(tree2))
    print('Different trees: ')
    print(tree1.isSimilar(tree3))
    print('Printing tree 1 level 3: ')
    print(tree1.printLevel(3))
    # Get the height of the two trees that are different
    print('Printing height of tree 1: ')
    print(str(tree1.getHeight()))
    # Get the number of nodes in the left and right subtree
    print('Number of left/right nodes in tree 1: ')
    print(str(tree1.numNodes()))
main()
