def Multiply(x,y,temp):
    x = x+temp
    y = y-1
    if y > 1:
        Multiply(x,y,temp)
    if y == 1:
        print(x)

def Multiplyfor(x,y):
    temp = x
    for i in range(y-1):
        x = x+temp
    print(x)

def main():
    Multiply(3,4,3)
    Multiplyfor(3,4)
main()
