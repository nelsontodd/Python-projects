#  File: Boxes.py

#  Description: This file makes list of nested boxes

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Partner Name: -

#  Partner UT EID: -

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 02/29/2016

#  Date Last Modified: 03/02/16
class Box (object):
    def __init__ (self, length = 0, width = 0, height = 0):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)
        self.total = self.length*self.width*self.height

    def __str__ (self):
        return '[' + str(self.length) + ', ' +str(self.width) +', ' +  str(self.height) + ']'


def sortboxes (boxlist):
    for k in range(len(boxlist)): #A simple bubble sort
        for j in range(len(boxlist)-(k+1)):
            if (boxlist[j].length+boxlist[j].width+boxlist[j].height) > (boxlist[j+1].length+boxlist[j+1].width+boxlist[j+1].height):
                tempVal = boxlist[j]
                boxlist[j] = boxlist[j+1]
                boxlist[j+1] = tempVal
    return boxlist
def checkBoxes (boxlist):
    for k in range(len(boxlist)-1): #A simple check to ensure all dimensions in this list of boxes work
        if boxlist[k+1].length <= boxlist[k].length:
            return False
        if boxlist[k+1].width <= boxlist[k].width:
            return False
        if boxlist[k+1].height <= boxlist[k].height:
            return False
    return True

def sub_sets (a, b, idx, unsortednestedboxes): #Finds all sub sets of the input and adds them to the unsortednestedboxes list if they are a nestedbox
  if (idx == len(a)):
          if checkBoxes(b) == True: #add to list if they are indeed nestable
              unsortednestedboxes.append(b)
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, c, idx + 1, unsortednestedboxes)
    sub_sets (a, b, idx + 1, unsortednestedboxes)

def main():
    listBoxes = []
    with open('Boxes.txt') as Inputlist: #open the boxes.txt file
        Inputtext = Inputlist.read().splitlines()
        map(int, Inputtext[0])
    for i in range(1,int(Inputtext[0])+1): #for each line of text, which represents a box
        temp = Inputtext[i].split()
        map(int, temp)
        for k in range(2): #A simple bubble sort
            for j in range(2-(k)):
                if temp[j+1] < temp[j]:
                    tempVal = temp[j]
                    temp[j] = temp[j+1]
                    temp[j+1] = tempVal
        Boxtemp = Box (temp[0],temp[1],temp[2]) #instantiate a new, sorted member of the nestedbox class
        listBoxes.append(Boxtemp) #add them onto this list
    sortedList = sortboxes(listBoxes) #make a sorted list of boxes
    a = sortedList
    b = []
    unsortednestedboxes = []
    nestedBoxeslist = []
    hugestr = ''
    sub_sets (a, b, 0,unsortednestedboxes) #This method gets and returns all nested boxes that are a subset of the given input
    longest = 0

    for k in range(len(unsortednestedboxes)-1): #Find the longest chain of nested boxes
        if len(unsortednestedboxes[k]) > len(unsortednestedboxes[k+1]):
            longest = len(unsortednestedboxes[k])
    if longest  > 1:
        print('Largest subset of nesting boxes:' + '\n')
        for s in range(len(unsortednestedboxes)): #print the output
            if len(unsortednestedboxes[s]) == longest: #print the nested box list if it is as long as the 'longest' var
                for h in unsortednestedboxes[s]:
                    print(h)
                print('\n')
    else:
       print('No nesting boxes!')
main()
