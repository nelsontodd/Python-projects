#  File: Triangle.py

#  Description: Finds the greatest path sum through three different methods

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 04/16

#  Date Last Modified:


import itertools
import math
from itertools import *
#def permutations0 (permutationsList,hi):
#    print(list(itertools.permutations(range(1),hi)))
#    return permutationsList
def make_sets(numberLines):
    masterList = [[0 for x in range(numberLines)]for k in range(numberLines+1)]
    count = 0
    for i in range(1,numberLines+1):
        count = count+1
        for j in range(count):
            masterList[i][j] = 1
    return masterList
# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    numSoln = 2**(len(grid))
    largestSum = 0;
    temp = 0
    index = 0
    for i in range(numSoln):
        temp = grid[0][0]
        index = 0
        for j in range(len(grid)-1):
            index = index + (i >> j & 1)
            temp = temp + grid[j + 1][index]

        if (temp > largestSum):
            largestSum = temp
    return largestSum
# returns the greatest path sum using greedy approach
def greedy (grid):
    total = 0
    n = 0
    total = total + grid[0][0]
    for i in range(1,len(grid)):
        total = total + max(grid[i][n],grid[i][n+1])
        if max(grid[i][n],grid[i][n+1]) == grid[i][n]:
            n = n
        else:
            n = n+1
        #print('Total, adding:'+ str(max(grid[i][n],grid[i][n+1])) + ' is '+str(total) + ' at index ' + str(n))
    return total

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid,rowNum):
    # iterate over the given row
    for i in range(len(grid[rowNum])):
        # add the largest of the values below-left or below-right
        grid[rowNum][i] = grid[rowNum][i]+ max([grid[rowNum+1][i],grid[rowNum+1][i+1]])
    # base case
    if len(grid[rowNum])==1:
        return grid[rowNum][0]
    # recursive case
    else:
        return rec_search(grid, rowNum-1)

# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):
    for i,j in [(i,j) for i in range(len(grid)-2,-1,-1) for j in range(i+1)]:
        grid[i][j] +=  max([grid[i+1][j],grid[i+1][j+1]])

    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def readFile (Input):
    numberLines = int(Input[0])
    grid = [[0 for x in range(numberLines)] for x in range(numberLines)]
    for i in range(1,numberLines+1):
        temp = Input[i].split()
        grid[i-1] = map(int,temp)
    return grid

def main ():
  # read triangular grid from file
  with open('triangle.txt') as Inputlist: #open the josephus.txt file
      Inputtext = Inputlist.read().splitlines()
      numberLines = int(Inputtext[0])
      GridAf = readFile(Inputtext)
  #print(str(GridAf))
  GridAf1 = [row[:] for row in GridAf]
  GridAf2 = [row[:] for row in GridAf]
  GridAf3 = [row[:] for row in GridAf]
  GridAf4 = [row[:] for row in GridAf]
  # output greates path from exhaustive search
  print('Exhaustive: '+str(exhaustive_search(GridAf1)))
  # output greates path from greedy approach
  print('Greedy: '+str(greedy(GridAf2)))
  #bigPerm1 = []
  #bigPerm = list(permutations(range(1),numberLines))
  #bigSet = make_sets(numberLines)
  #print(len(bigSet))
  #print(bigPerm)
  #for i in range(1,len(bigSet)):
    #  permutation = []
     # print('pass #: ' + str(i))
      #permutationos(bigSet[i],0,numberLines-1, permutation)
      #bigPerm[i] = permutation
  #realTotals = []
  #print(list(permutations(range(2),7)))
  #print(bigPerm[5])
  #for u in range(numberLines):
      #print('pass #: ' + str(u))
      #realTotals.append(exhaustive_search(GridAf,bigPerm[u]))
  #print(max(realTotals))
  #output greates path from divide-and-conquer approach
  print('Recursive approach: ' + str(rec_search(GridAf3,len(GridAf3)-2)))
  # output greates path from dynamic programming
  print('Dynamic Approach: '+str(dynamic_prog(GridAf4)))
main()
