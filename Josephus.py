#  File: Josephus.py

#  Description: Deletes the link specified by "drawing lots" (Choosing an element and counting n entries after)

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Partner Name: -

#  Partner UT EID: -

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 04/07/16

#  Date Last Modified:

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
      return str(self.data)
class CircularList (object):
  def __init__ (self):
    self.first = None
    self.last = None

    # Insert an element in the list
  def insert ( self, item ):
      newLink = Link(item)
      temp = self.first.next
      self.first.next = newLink
      newLink.next = temp

  # Find the link with the given key
  def find ( self, key ):
      current = self.first
      while current.data != key:
          current = current.next
      return current
  # Delete a link with a given key
  def delete ( self, key ):
      current1 = key
      if (current1 == None):
        return None
      current = self.first
      while (current1 != current):
        if (current.next == self.first):
          return None
        elif current.next == current1: #Removes the current link and the previous takes its place
            previous = current
            current = current.next
            if(current == self.last): #special case if the link to be deleted is the last
                self.last = previous
            after = current.next
            current = None
            previous.next = after

            return self
        else:
            current = current.next
      if current1 == self.first: # Special case if the link we need is the first.
          current2 = self.last
          current = current2.next
          after = current.next
          self.first = after
          self.last.next = after
          current = None
          return self
  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n,deadList ):
      current = self.first
      if isinstance(start,Link): #The first one is not a link
          while current != start:
              current = current.next
      else:
          for k in range(start-1): #find the start
              current = current.next
      for i in range(n-1): #Count up from the start
          current = current.next
      counter = current.next
      deadList.append(str(current))
      self.delete(current)
      counter = counter.next
      return counter #Return the index we need to start counting at
  def __str__ (self):
      returnstr = ''
      current = self.first
      while (current.next != self.first):
          returnstr = returnstr + str(current) + ' '
          current = current.next
      returnstr = returnstr+str(current)
      return returnstr
  def insertFirst (self, data):
    newLink = data
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    if self.last == None and self.first == None:
        self.last = newLink
        self.first = newLink
    else:
        self.last.next = newLink
        self.last = newLink
        self.last.next = self.first

  # get number of links
  def getNumLinks (self):
      self.numlinks = 0
      current = self.first
      while (current.next != self.first):
          self.numlinks = self.numlinks+1
          current = current.next
      return self.numlinks
  # Add data at the beginning of the list
  def addFirst (self, data):
      for i in range(len(data)):
          self.insertFirst(data[i])
      self.insertLast(data[len(data)-1])
      return self
  # Add data at the end of a list
  def addLast (self, data):
      for i in range(len(data)):
          self.insertLast(data[i])
      return self
  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
      self.addLast(data)
      self  = self.sortList()

def main():
    with open('josephus.txt') as Inputlist: #open the josephus.txt file
        Inputtext = Inputlist.read().splitlines()
        numberSoldiers = int(Inputtext[0])
        start = int(Inputtext[1])
        adder = int(Inputtext[2])
        soldierList = []
        for i in range(numberSoldiers):
            soldierList.append(i+1)
        soldiers = CircularList()
        soldiers.addLast(soldierList)
        deadList = []
        while soldiers.getNumLinks() > 0:
            index = soldiers.deleteAfter(start,adder,deadList)
            begin = soldiers.first
            while begin.next != index:
                begin = begin.next
            start = begin
        deadstr = ''
        for i in range(len(deadList)):
            deadstr+=str(deadList[i])+' '
        print(deadstr + '\n')
        print(str(soldiers))
main()
