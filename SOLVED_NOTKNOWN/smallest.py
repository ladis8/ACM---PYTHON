
from sys import stdin

import math


def nCr(n,r):
    a = max (r, n-r)
    counter = n
    out =1
    while True:
        if (counter != a):
            out *=counter
            counter-=1
        else:
            break
    return out/math.factorial(n-a)



def count (a,b):

    out = (nCr(13, a) * nCr(13,b)) /nCr(26, a+b)
    if a!=b:
        out*=2

    print ("%d-%d split: %.8f" %(a,b,out))





if __name__ == '__main__':

    line = stdin.readline().rstrip()
    while True:
        try:
            a = int(line.split()[0])
            b = int(line.split()[1])
            count(a,b)
            line = stdin.readline().rstrip()
            if line == "-1 -1":
                break



        except EOFError:
            break


