from pythonds.basic.stack import Stack
def g(st, idx):
    if idx == len(st)-1:
        return int(st[idx]) * 2**0*1
    else:
        n = len(st)-1
        print(n)
        return g(st, idx+1) + (2**(n-idx)) * (int(st[idx]))



rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

print('g:' + str(g('1101', 0)))
