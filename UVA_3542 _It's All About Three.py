
import math

scale = 1000000

array = [False] * scale
primes = [False] * scale


def factorize(number):
    n = number
    dividers = set()
    for i in range(2, int (math.sqrt(number))+2):
        if primes[i] and n % i == 0:
            dividers.add(i)
            while (n % i == 0):
                n = n / i
            if n == 0:
                break
    return dividers


for i in range(2,scale):
    s = factorize (i)
    if len(s)==0:
        primes[i] = True
        if i %10 ==3:
            array [i] = True
    else:
        state = True
        for divider in s:
            if divider%10 !=3:
                state = False
        array[i] = state
#print (primes)
#print(array)

f = open("a.out.txt", 'w')

for i,y in enumerate(array):
    f.write("1,") if y else f.write("0,")





