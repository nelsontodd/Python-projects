#  File: TestLinkedList.py

#  Description: Linked list class

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Partner Name: -

#  Partner UT EID: -

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 03/30

#  Date Last Modified:


class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
      return str(self.data)
class LinkedList (object):
  def __init__ (self):
    self.first = None
  def __str__ (self):
      returnstr = ''
      current = self.first
      while (current.next != None):
          returnstr = returnstr + str(current) + ' '
          current = current.next
      return returnstr
  def insertFirst (self, data):
    newLink = Link (data)

    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)

    current = self.first
    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink (self, data):

      current = self.first
      previous = self.first

      if (current == None):
          return None

      while (current.data != data):
          if (current.next == None):
              return None
          else:
              previous,current = current,current.next


      if (current == self.first):
          self.first = self.first.next
      else:
          previous.next = current.next

      return current
  # get number of links
  def getNumLinks (self):
      self.numlinks = 0
      current = self.first
      while (current.next != None):
          self.numlinks = self.numlinks+1
          current = current.next
      return self.numlinks+1
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
      self.insertLast(data[len(data)-1])
      return self
  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
      self.addLast(data)
      self  = self.sortList()
  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
      current = self.first
      if (current == None):
        return None

      while (current.data != data):
        if (current.next == None):
          return None
        elif current.next.data == data:
            previous = current
            current = current.next
            after = current.next
        else:
            current = current.next

      current = None
      previous.next = after

      return self
  # Copy the contents of a list and return new list
  def copyList (self):
      listlinks = LinkedList()
      current = self.first
      while current != None:
          listlinks.insertLast(current.data)
          current = current.next
      return listlinks
  # Reverse the contents of a list and return new list
  def reverseList (self):
      listlinks1 = LinkedList()
      current = self.first
      while current != None:
          listlinks1.insertFirst(current.data)
          current = current.next
      listlinks1.insertLast(self.first)
      listlinks1.first = listlinks1.first.next
      return listlinks1
  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
      if self.first == None:
          return None
      current=self.first.next
      while current != None:
          current = current.next
          if current == None:
              break
          sortedList= self.first
          while(sortedList != current):
              if current.data<sortedList.data:
                  if current.next == None:
                      sortedList = current
                  else:
                      temp = current.data
                      current.data = sortedList.data
                      sortedList.data = temp

              else:
                sortedList = sortedList.next
      return self

  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
      listlinks = LinkedList()
      current = self.first
      while current != None:
          listlinks.insertLast(current.data)
          current = current.next
      listlinks = listlinks.sortList()
      current = self.first
      other = listlinks.first
      Sorted = True
      while Sorted and current != None:
          if current.data != other.data:
              Sorted = False
          else:
              current = current.next
              other = other.next
      return Sorted


  # Return True if a list is empty or False otherwise
  def isEmpty (self):
      if self.first == None:
          return True
      else:
          return False

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
      current = self.first
      other = b.first
      newlist = LinkedList()
      while current != None or other != None:
          while current.next == None and other.next != None:
              #print('here 1')
              newlist.insertLast(other.data)
              other = other.next
          while other.next == None and current.next != None:
             # print('here 2')
              newlist.insertLast(current.data)
              current = current.next
          if current.next == None:
              #print('here 3')
              current = current.next
          if other.next == None:
              #print('here 4')
              other = other.next
          if other != None and current != None:
              if current.data < other.data:
                  #print(str(current.data))
                  newlist.insertLast(current.data)

                  while current.next.data <= other.data:
                     # print('here')
                      current = current.next
                      newlist.insertLast(current.data)

                      if current.data >= other.data:
                          #print(str(other.data))
                         # print('while loop insert 1' + str(other.data))
                          newlist.insertLast(other.data)
                          other = other.next
                          #print('Current1: '+ str(current.data) + 'Other1: ' + str(other.data))
                          break
                  current = current.next

              if current.data >= other.data:
                 # print(str(other.data))
                  newlist.insertLast(other.data)
                  while other.next.data <= current.data:
                      other = other.next
                      newlist.insertLast(other.data)
                      if other.data > current.data:
                          #print('while loop insert 2' + str(other.data))
                          newlist.insertLast(current.data)
                          current = current.next
                          #print('Current2: '+ str(current.data) + 'Other2: ' + str(other.data))
                          break
                  other = other.next
      return newlist
  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
      current = self.first
      other = b.first
      Equal = True
      while Equal and current != None:
          if current.data != other.data:
              Equal = False
          else:
              current = current.next
              other = other.next
      return Equal
  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
      current = self.first
      other = self
      other1 = other.first
      while current != None:
          while other1 != None:
              if current.data == other1.data:
                  self.delete(current)
                  other1 = other1.next
              else:
                  other1 = other1.next
          current = current.next
      return self
def main():
  # Test methods addFirst() and __str__() by adding more than
  # 10 items to a list and printing it.
  linkedlist1 = LinkedList()
  regularlist = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
  linkedlist3 = LinkedList()
  linkedlist3.addFirst(regularlist)
  print('Linked List created with addFirst: ' + str(linkedlist3))
  # Test method addLast()
  linkedlist2 = LinkedList()
  regularlist2 = [13, 78, 90, 43, 48]
  linkedlist2.addLast(regularlist2)
  linkedlist1.addLast(regularlist)
  print('Linked List created with addlast: ' + str(linkedlist1))
  # Test method addInOrder()
  linkedlist4 = LinkedList()
  linkedlist4.addInOrder(regularlist)
  print('Linked List created with addInOrder: ' + str(linkedlist4))
  # Test method getNumLinks()
  print('Number of links: ' + str(linkedlist1.getNumLinks()))
  # Test method findUnordered()
  # Consider two cases - item is there, item is not there
  print('findUnordered (there): ' + str(linkedlist1.findUnordered(23)))
  print('findUnordered (not there): ' + str(linkedlist1.findUnordered(95)))
  # Test method findOrdered()
  # Consider two cases - item is there, item is not there
  print('findOrdered (there): ' + str(linkedlist1.findOrdered(23)))
  print('findOrdered (not there): ' + str(linkedlist1.findOrdered(95)))
  print('Number of links: ' + str(linkedlist1.getNumLinks()))
  # Test method delete()
  # Consider two cases - item is there, item is not there
  print('Delete: '+ str(linkedlist1.delete(23)))
  # Test method copyList()
  print('Copied List: ' + str(linkedlist1.copyList()))
  # Test method reverseList()
  print('Reversed List: ' + str(linkedlist1.reverseList()))

  # Test method sortList()
  print('Sorted List: ' + str(linkedlist1.sortList()))

  # Test method isSorted()
  print('Is sorted: ' + str(linkedlist1.isSorted()))
  # Consider two cases - list is sorted, list is not sorted

  # Test method isEmpty()
  print('Is empty: ' + str(linkedlist1.isEmpty()))
  linkedlist2 = linkedlist2.sortList()
  # Test method mergeList()
  print('Merge with list ' +str(linkedlist2)+' :'+ str(linkedlist1.mergeList(linkedlist2)))
  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print('IsEqual: '+ str(linkedlist1.isEqual(linkedlist2)))
  print('IsEqual: '+ str(linkedlist1.isEqual(linkedlist1)))
  # Test removeDuplicates()
  print('removeDuplicates: '+ str(linkedlist1.removeDuplicates()))
main()
