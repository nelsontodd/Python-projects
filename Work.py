#  File: Work.py

#  Description: Modified binary search that reads lines from a file and outputs minimum effort for a project

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 03/25

#  Date Last Modified: 03/25/16


def binaryFinder (a, x, k):
  count = 0
  total = 0
  total1 = 1
  listAns = []
  listpows = []
  while x - (total1*k) > 1: # Find all the powers of k we could use for this
      total1 = k**count
      count = count+1
  for i in range(0, count): # make a list
          listpows.append(k**i)
 # print('List: ' + str(listpows))
  for p in range(x, 1, -1): #decrement from x down
      total = 0
      for j in range(len(listpows)):
          total = total + p//listpows[j] # Add this number p // k as many times as necessary
          if total == x or total == (x+1): #if it equals the total we need then add it to the list
              listAns.append(p)
  return min(listAns) #return the smallest which signifies least amount of effort
def main():
    with open('work.txt') as wakka: #We need to read from the nim.txt file. No error handling.
        Inputtext = wakka.read().splitlines()
        map(int, Inputtext[0])
    for i in range(1,int(Inputtext[0])+1): #for each line of text, which represents a box
        temp = Inputtext[i].split()
        n = int(temp[0]) #get number of lines
        k = int(temp[1]) #get productivity factor
        listNums = []
        for i in range(0,n):
            listNums.append(i+1)
        print(binaryFinder (listNums, n, k))
main()
