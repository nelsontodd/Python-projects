
#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked
#  list having the row, column, and non-zero data in each link

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 04/13

#  Date Last Modified:

class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None

  def __str__ (self):
    s = ''
    return s

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row		# number of rows
    self.num_cols = col		# number of columns
    self.matrix = None

  # setElement() perform an assignment operation a[i][j] = value
  # if value is 0 the link if it exists is deleted
  # if value is non zero then the current value is updated if a
  # link already exists or a new link is added
  def setElement (self, row, col, data):
    if (data == 0):
      self.deleteLink (row, col)
    else:
      self.insertLink (row, col, data)

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create a new link
    newLink = Link (row, col, data)
    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
        previous = current
        current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
        previous.next = newLink
        newLink.next = current
        return

    # on the row, search by column
    while ((current != None) and (current.col < col)):
        previous = current
        current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
        current.data = data
        return
    # now insert newLink
    previous.next = newLink
    newLink.next = current
  # deletes and returns a Link if it is there or None otherwise
  def deleteLink (self, row, col):
    current = self.matrix
    if current == None:
        return
    while current.row != row:
        if current == None:
            return None
        current = current.next
    while current.next.col != col:
        if current == None:
            return None
        current = current.next
    previous = current
    current = current.next
    after = current.next
    current = None
    previous.next = after
    return self
  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.row < row_num)):
      current = current.next

    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a

    if ((current != None) and (current.row == row_num)):
        for j in range (self.num_cols):
            if ((current != None) and current.col == j):
                a.append (current.data)
                current = current.next
            else:
                a.append (0)
    return a

  # return a column of the sparse matrix
  def getCol (self, col_num):
      # create a blank list
      a = []

      # search for the row
      current = self.matrix
      if (current == None):
          return a
      while current != None:
          if ((current != None) and (current.col == col_num)):
              a.append (current.data)
          if current.next != None:
              if current.col +1 == col_num and current.next.col != col_num:
                  a.append(0)
          if current.col+1 == col_num and current.next == None:
              a.append(0)
          current = current.next
      return a

  # add two sparse matrix
  def __add__ (self, other):
      current = self.matrix
      adder = other.matrix
      dim1 = 0
      dim2 = 0
      if self.num_cols >= other.num_cols:
          dim2 = self.num_cols
      else:
          dim2 = other.num_cols
      if self.num_rows >= other.num_rows:
          dim1 = self.num_rows
      else:
          dim1 = other.num_rows
      result = SparseMatrix(dim1,dim2) #create a new matrix of the proper dimensions
      while current != None and adder != None:
          if current.row == adder.row and current.col == adder.col: #if they can be added, add them and increment both
              result.insertLink(current.row, current.col, (current.data + adder.data))
              adder = adder.next
              current = current.next
          elif (current.row == adder.row and current.col < adder.col) or current.row < adder.row: #add current if it is correct
              result.insertLink(current.row, current.col, current.data)
              current = current.next
          elif (current.row == adder.row and adder.col < current.col) or adder.row < current.row: # add 'adder' if it is correct to add
              result.insertLink(adder.row, adder.col, adder.data)
              adder = adder.next

      while current != None: #add any leftovers
          result.insertLink(current.row, current.col, current.data) 
          current = current.next
      while adder != None: #add any leftovers
          result.insertLink(adder.row, adder.col, adder.data)
          adder = adder.next
      return result
  # multiply two sparse matrices
  def __mul__ (self, other):
      current = self.matrix
      adder = other.matrix
      dim1 = self.num_rows
      dim2 = other.num_cols
      if self.num_cols != other.num_rows: #Make sure that the matrices can be multiplied
          return None
      result = SparseMatrix(dim1,dim2)
      for i in range(self.num_rows): #Perform for each row_num
          Product = []
          rows = self.getRow(i)
          for k in range(other.num_cols): #for each column in the other matrix
              cols = other.getCol(k)
              producto = 0
              for p in range(len(cols)): #for each element in that column
                  producto = producto + cols[p] * rows[p]
              if producto != 0:
                  result.insertLink(i,k,producto) #insert the product
      return result

  # return a string representation of the matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data).rjust(3, ' ')
          current = current.next
        else:
          s = s + "0".rjust(3, ' ')
      s = s + "\n"
    return s

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.insertLink (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Element to Zero")
  matA.setElement (1, 1, 0)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(1)
  print (col)

  inFile.close()

main()
