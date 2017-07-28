from sys import stdin


def convertnumber(number):
    n = len(str(number))
    array =[]
    for i in range (n):
        array.append(int(number%10))
        number= int (number/10)
    return list(reversed(array))


for line in stdin:
    try:
        b,n = map(int,line.split())
        if n==1:
            out = b-1
        elif n==2:
            out = b*(b-1) -1
        else:
            out=  (b-1)* b**(n-1) -(b-1)*b**(n-3)*(n-2) -(n-2)*b
        print (out)

    except EOFError:
        break


