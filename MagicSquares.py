#  File: MagicSquares.py

#  Description: Fills in a magic square for any odd number of entries, 'n'.

#  Student's Name: Nelson Morrow

#  Student's UT EID: ntm432

#  Partner's Name: tfwnofriends

#  Partner's UT EID: -

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/06/2016

#  Date Last Modified: 02/06/2016
import numpy as np
class makeSquare (object):

    def __init__(self, n=3):
        self.rowSum = 0;
        self.Size = n
        self.array = np.zeros((n,n), dtype=int)

    def OrderSquare(self): # This function fills in values to the square.
        number = 2;
        Column = ((self.Size-1))/2
        Row = self.Size-1
        Bounds = self.Size-1
        self.array[Row,Column] = 1
        for i in range(2,(self.Size)*(self.Size)+1): # Iterating from 2 to n.

            Vtemp = Row
            Htemp = Column

            if Row < Bounds: # To the right
                Row = Row+1
            else:
                Row = 0

            if Column < Bounds: # Slide down
                Column = Column+1
            else:
                Column = 0

            if Vtemp == Bounds and Htemp == Bounds: #if bottom right, place next value up.
                Vtemp = Vtemp-1
                Row = Vtemp
                Column = Htemp
                self.array[Vtemp,Htemp] = i
            elif int(self.array[Row,Column]) == 0: #Place i value into Row, Column
                self.array[Row,Column] = i
            else:                                  #Place i value up if number in the way
                Vtemp = Vtemp-1
                Row = Vtemp
                Column = Htemp
                self.array[Vtemp,Htemp] = i

    def printSquare(self): # This function returns a right justified magic square.
        prettySquare = ''
        for i in range(0,(self.Size)):
            for j in range(0,(self.Size)):
                prettySquare += str(self.array[i,j]).rjust(3, ' ')
                self.rowSum += self.array[i,j]
            prettySquare += '\n'
        print('Here is a ' + str(self.Size) + ' x' +' '+ str(self.Size)  + ' magic square:' + '\n' + '\n' + prettySquare)

    def checkSquare ( self ): # This function checks to ensure the Square is magic.
        columnSum = 0
        for i in range(0,(self.Size)):
            for j in range(0,(self.Size)):
                columnSum += self.array[j, i]
        ULLRSum = 0
        j = 0
        for i in range(0,self.Size):
                ULLRSum += self.array[j, i]
                j = j+1
        URLLSum = 0
        j = 0
        for i in range((self.Size)-1, -1, -1):
                URLLSum += self.array[j,i]
                j = j+1
        print('Sum of row = ' + str(self.rowSum/self.Size))
        print('Sum of column = ' + str(columnSum/self.Size))
        print('Sum diagonal (UL to LR) = ' + str(ULLRSum))
        print('Sum diagonal (UR to LL) = ' + str(URLLSum))

def getInput(): #This function gets user input, filtering for odd integers.

    try:
        n = int(input("Please enter an odd number: "))
        if n % 2 != 0:
            MagicSquare = makeSquare(n)
            makeSquare.OrderSquare(MagicSquare)
            makeSquare.printSquare(MagicSquare)
            makeSquare.checkSquare(MagicSquare)
        else:
            print('Number was not odd.'+ '\n')
            getInput()
    except ValueError:
            print('Please try again')
            getInput()
    except NameError:
            print('Please try again')
            getInput()
def main():
    getInput()
main()
