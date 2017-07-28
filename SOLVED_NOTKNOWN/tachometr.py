from sys import stdin

array = [1]

for i in range (10):
    array.append(9*array[i]+ int (pow(10.0, i+1)))
    #print (array[i])



def tacho(input):
    l = len(input)
    out =0
    for i in range(l):
        digit = int(input[i])

        if digit >4:
            sub =1
            for x in range(l-i-1):
                sub*=10
            out+=sub
        if digit <4 and i != l-1:
             out += digit * array[l-i-2]
        if digit >4 and i != l-1:
            out += (digit -1) * array[l -i -2]
    #print(out)
    print (input,end= "")
    print(": ", end="")
    print (int (input) - out)



def init ():
    line = stdin.readline().rstrip()
    while line !="0":
        try:
           tacho(line)
           line = stdin.readline().rstrip()
        except EOFError:
            break

init()
