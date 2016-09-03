#  File: BST_Cipher.py

#  Description: Encrypts things

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 04/30

#  Date Last Modified:


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      lower = encrypt_str.lower()
      stripped = lower.strip('!!')
      seen = []
      finalList = []
      encrypt_list = [ord(c) for c in stripped] #make a tree of ascii characters and remove duplicates
      for i in encrypt_list:
          if i not in seen:
              seen.append(i)
              finalList.append(i)
      self.root = None
      for i in range(len(finalList)):
          self.insert(finalList[i])
  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
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
          current = current.lChild
	else:
	  current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lChild)
      print aNode.data
      self.inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print aNode.data
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print aNode.data

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
	isLeft = True
      else:
        deleteNode = deleteNode.rChild
	isLeft = False

    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
	successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
	successor.rChild = deleteNode.rChild

    return True

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, key):
    current = self.root
    string = ''
    if ord(key) == current.data:
        return '*!'
    while ((current != None) and (current.data != ord(key))):
      if (ord(key) < current.data):
        current = current.lChild
        string+='<'
      else:
        current = current.rChild
        string+='>'
    string+='!'
    return string

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
      current = self.root
      if st == '*':
          return str(chr(current.data))
      for i in st:
          if i == '<':
              current = current.lChild
          if i == '>':
              current = current.rChild
      return str(chr(current.data))
  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      encryptedStr = ''
      stlower = st.lower()
      stlist = []
      for i in stlower:
          if i.isalpha() == True or ord(i) == 32: #cut out everything that isn't a letter or space
              stlist.append(i)
      for p in stlist:
          encryptedStr+=self.search(p)
      encryptedStr = encryptedStr[:-1]
      return encryptedStr
  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
      stList = st.split('!')
      decryptedStr = ''
      for i in stList:
          decryptedStr += self.traverse(i)
      return decryptedStr
def main():
    str1 = 'the quick brown fox jumps over the lazy dog'
    str2 = raw_input("Enter a string to be encrypted: ")
    tree1 = Tree(str1)
    #tree1.inOrder(tree1.root)
    print('Encrypted String: '+tree1.encrypt(str2))
    str3 = raw_input("Enter a string to be decrypted: ")
    print('Decrypted String: '+tree1.decrypt(str3))
main()
