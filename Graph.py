from __future__ import print_function
#  File: Graph.py

#  Description:

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 05/08

#  Date Last Modified:
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()
  def __str__(self):
      returnStr = ''
      for item in self.stack:
          #print(str(item))
          returnStr += str(item)
      return returnStr
  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)

'''
class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):

  def __le__ (self, other):

  def __gt__ (self, other):

  def __ge__ (self, other):

  def __eq__ (self, other):

  def __ne__ (self, other):
'''

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # given a label get the index of a Vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  def getAdjVisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and ((self.Vertices[i]).wasVisited()):
        return i
    return -1

  # does a depth first search in a graph
  def dfs (self, v):
    # create a stack
      theStack = Stack()

    # mark vertex as visited and push on the stack
      (self.Vertices[v]).visited = True
      print (self.Vertices[v])
      theStack.push (v)

      while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex(theStack.peek())
          if (u == -1):
              u = theStack.pop()
          else:
              (self.Vertices[u]).visited = True
              print (self.Vertices[u])
              theStack.push(u)

    # the stack is empty, let us reset the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
          (self.Vertices[i]).visited = False
  # does a breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        if self.Vertices[v2] != None:
            theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
      if self.adjMat[self.getIndex(toVertexLabel)][self.getIndex(fromVertexLabel)] != 0:
          return self.adjMat[self.getIndex(toVertexLabel)][self.getIndex(fromVertexLabel)]
      if self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] != 0:
          return self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]
      return -1
  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
      neighbors = []
      for i in range(len(self.adjMat[self.getIndex(vertexLabel)])):
          if self.adjMat[self.getIndex(vertexLabel)][i] != 0:
              neighbors.append(str(self.Vertices[i]))
      return neighbors
  # get a copy of the list of vertices
  def getVertices (self):
      Vertices = []
      for i in self.Vertices:
          Vertices.append(i.label)
      return str(Vertices)
  # determine if a directed graph has a cycle
  def hasCycle (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if self.getAdjVisitedVertex (u) != -1:
          return True
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push(u)

    # stack is empty reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return False
  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
      self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] = 0
  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
      #print(self.getIndex(vertexLabel))
      del self.adjMat[self.getIndex(vertexLabel)]
      for i in range(len(self.adjMat)):
          del self.adjMat[i][self.getIndex(vertexLabel)]
      del self.Vertices[self.getIndex(vertexLabel)]
  # return a list of vertices after a topological sort
  def toposort (self, v,sortStack):
    # create a stack
      theStack1 = Stack()
    # mark vertex as visited and push on the stack
      (self.Vertices[v]).visited = True
      #print (self.Vertices[v])
      sortStack.push((self.Vertices[v]).label)
      theStack1.push (v)
      while (not theStack1.isEmpty()):
      # get an adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex(theStack1.peek())
          if (u == -1):
              u = theStack1.pop()
          else:
              (self.Vertices[u]).visited = True
              #print (self.Vertices[u])
              sortStack.push((self.Vertices[u]).label)
              theStack1.push(u)
      for item in self.Vertices:
          if item.visited == False:
              self.toposort(self.getIndex(item.label),sortStack)
      return str(sortStack)
    # the stack is empty, let us reset the flags

  # prints a list of edges in ascending order of their weights
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def edgeList (self):
      listEdges = []
      nVert = len (self.Vertices)
      for i in range (nVert):
          for j in range (nVert):
             if self.adjMat[i][j] != 0:
                 listEdges.append(str(self.Vertices[i]))
                 listEdges.append(str(self.Vertices[j]))
      edgeStr = ''
      while j < len(listEdges):
          i = 0
          while i < len(listEdges)-3:
              if self.getEdgeWeight(listEdges[i],listEdges[i+1]) > self.getEdgeWeight(listEdges[i+2],listEdges[i+3]):
                  temp = listEdges[i+2]
                  temp1 = listEdges[i+3]
                  listEdges[i+2] = listEdges[i]
                  listEdges[i+3] = listEdges[i+1]
                  listEdges[i] = temp
                  listEdges[i+1] = temp1
              i+=2
          j+=1
      #print(str(listEdges))
      i = 0
      while i <(len(listEdges)):
          edgeStr = edgeStr+ str(listEdges[i]) + ' - ' + str(listEdges[i+1]) + ', '
          i = i+2
      return edgeStr
def main():
  # Create Graph object
  cities = Graph()

  # Open file for reading
  inFile = open ("./graph.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)
    cities.addVertex (city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  #print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    cities.addDirectedEdge (start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  #print (startVertex)

  # Close file


  # print the adjacency matrix
  nVert = len (cities.Vertices)
  for i in range (nVert):
    for j in range (nVert):
      print(cities.adjMat[i][j], end=' ')
    print()
  print ()

  # test depth first search
  print("Depth First Search from Houston")
  cities.dfs (cities.getIndex('Houston'))
  print()

  # test breadth first search
  print("Breadth First Search from Houston")
  cities.bfs (cities.getIndex('Houston'))

  # test if a directed graph has a cycle
  letters = Graph()

  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    letter = (inFile.readline()).strip()
    print (letter)
    letters.addVertex (letter)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    letters.addDirectedEdge (start, finish, weight)

  nVert = len (letters.Vertices)
  for i in range (nVert):
      for j in range (nVert):
          print(letters.adjMat[i][j], end=' ')
      print()
  print ()
  startVertex = (inFile.readline()).strip()
  print("Start Vertex: "+startVertex)
  # Read the starting vertex for dfs, bfs, and shortest path
  print("Depth First Search from B: ")
  letters.dfs(letters.getIndex(startVertex))
  print("Breadth First Search from B: ")
  letters.bfs(letters.getIndex(startVertex))
  print("Has cycle: "+str(letters.hasCycle(letters.getIndex(startVertex))))
  print('Deleted edge from B to F')
  letters.deleteEdge('B','F')
  nVert = len (letters.Vertices)
  for i in range (nVert):
      for j in range (nVert):
          print(letters.adjMat[i][j], end=' ')
      print()
  print ()
  print('Removed Vertex A')
  letters.deleteVertex('A')
  nVert = len (letters.Vertices)
  for i in range (nVert):
      for j in range (nVert):
          print(letters.adjMat[i][j], end=' ')
      print()
  print ()
  print("Has a cycle: "+ str(letters.hasCycle(letters.getIndex(startVertex))))
  # test deletion of an edge
  #print(letters.getVertices())
  print('Topological sort: ')
  sortStack = Stack()
  print(letters.toposort(letters.getIndex('C'),sortStack))
  # test deletion of a vertex
  #letters.deleteVertex('A')
  # test topological sort
  # test edge list in ascending order of weights
  print(letters.edgeList())

main()
