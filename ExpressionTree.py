#  File: ExpressionTree.py

#  Description: Takes equations and makes them into expression trees

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 04/22

#  Date Last Modified:
class Stack (object):
  def __init__ (self):
    self.stack = []
  def __str__ (self):
    returnStr = ''
    for i in range(len(self.stack)):
        returnStr += str(self.stack[i])
    return returnStr
  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )
  def push0(self, item):
    self.stack.insert ( 0,item )
  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()
  def pop0 (self, place = 0):
    rreturn = self.stack[place]
    self.stack.remove(self.stack[place])
    return rreturn
  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)
  def total(self):
      total = Stack()
      total = self
      operators = ['+','-','*','/']
      i = 0
      while i < len(total.stack):
          #print(str(i) + str(total))
          if total.stack[i] in operators:
              oper1 = int(total.pop0(i-2))
              i -=1
              oper2 = int(total.pop0(i-1))
              i-=1
              token = total.pop0(i)
              i-=1
              if token == '+':
                  total.push0(oper1 + oper2)
              if token == '-':
                  total.push0(oper1 - oper2)
              if token == '/':
                  total.push0(oper1 / oper2)
              if token == '*':
                  total.push0(oper1 * oper2)
          i = i+1
      return str(total)
  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))
class Node (object):
    def __init__ (self, data, childLeft = None,childright = None):
        self.data = data
        self.childLeft = childLeft
        self.childRight = childRight

def postFix (Input):
    Inputl = list(Input.split())
    #print(Inputl)
    countParentheses = []
    tempCount = 0
    operators = ['+','-','/','*']
    postStack = Stack()
    i = 0
    numThings = 0
    for k in range(len(Inputl)):
        if Inputl[k] != '(' and Inputl[k] != ')':
            #print(str(Inputl[k]))
            numThings+=1
    #print(str(numThings))
    while numThings > 0 and i <=len(Inputl):
        #print(str(i)+ ' length: ' + str(len(Inputl)))
        i=i+1
        if Inputl[i] == ')':
            p = i
            #print(str(i))
            count = 0
            #print(str(Inputl))
            while Inputl[p] not in operators:
                p = p-1
            if Inputl[p-1] != '(' and Inputl[p-1] != ')':
                postStack.push(Inputl[p-1])
                Inputl.remove(Inputl[p-1])
                numThings-=1
                p = p-1
                count = count+1
            if Inputl[p+1] != '(' and Inputl[p+1] !=')':
                postStack.push(Inputl[p+1])
                Inputl.remove(Inputl[p+1])
                numThings-=1
                count = count+1
            if Inputl[p] != '(' and Inputl[p] != ')':
                postStack.push(Inputl[p])
                Inputl.remove(Inputl[p])
                numThings-=1
                p = p-1
                count = count+1
            #print(str(Inputl))
            i = i-count
    return postStack

def preFix (Input):
    Inputl = list(Input.split())
    #print(Inputl)
    countParentheses = []
    tempCount = 0
    operators = ['+','-','/','*']
    preStack = Stack()
    i = len(Inputl)-1
    numThings = 0
    for k in range(len(Inputl)):
        if Inputl[k] != '(' and Inputl[k] != ')':
            #print(str(Inputl[k]))
            numThings+=1
    #print(str(numThings))
    while numThings > 0 and i >= 0:
        #print(str(i)+ ' length: ' + str(len(Inputl)))
        i=i-1
        if Inputl[i] == '(':
            p = i
            #print(str(i))
            count = 0
            #print(str(Inputl))
            while Inputl[p] not in operators:
                p = p+1
            if Inputl[p+1] != '(' and Inputl[p+1] != ')':
                preStack.push(Inputl[p+1])
                Inputl.remove(Inputl[p+1])
                numThings-=1
                count = count+1
            if Inputl[p-1] != '(' and Inputl[p-1] !=')':
                preStack.push(Inputl[p-1])
                Inputl.remove(Inputl[p-1])
                p = p-1
                numThings-=1
                count = count+1
            if Inputl[p] != '(' and Inputl[p] != ')':
                preStack.push(Inputl[p])
                Inputl.remove(Inputl[p])
                numThings-=1
                p = p-1
                count = count+1
            #print(str(Inputl))
            #i = i-count
    return preStack

class Tree (object):
  def __init__ (self):
      self.root = None
  def createTree (self, expr):
      operators = ['+','-','/','*']
      for i in range(len(expr)):
          if expr[i] in operators:
              if i == 0:
                  self.root = expr[i]
  def evaluate (self, aNode):
      print('')
  def preOrder (self, aNode):
      print('')
  def postOrder (self, aNode):
      print('')
def main():
    lines = [line.rstrip('\n') for line in open('input.txt')]
    for j in range(len(lines)):

        post = postFix(lines[j])
        pre = preFix(lines[j])
        preString = ''
        i = len(pre.stack)
        while i > 0:
            i-=1
            preString += str(pre.stack[i])+ ' '
        k = 0
        postString = ''
        while k < len(post.stack):
            postString += str(post.stack[k])+ ' '
            k +=1
        print(lines[j] + ' = '+str(post.total()))
        print('Prefix Expression: '+preString)
        print('Postfix Expression: '+postString + '\n')

main()
