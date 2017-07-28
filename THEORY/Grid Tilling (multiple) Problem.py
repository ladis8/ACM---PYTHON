
#SPOJ GNY07H - Tiling a Grid With Dominoes 4x N
#UVA 10918 - Tri Tiling 3x N

maximumN = 1000
solution = []
fsol = []
gsol =[]

def readinput ():


    #SPOJ 4xN
    global solution
    solution = [-1 for _ in range(maximumN+1)]
     #4 init variables for n-4
    solution [0] = 0
    solution [1] = 1
    solution [2] = 5
    solution [3] = 11
    solution [4] = 36

    tests = int (input())
    for i in range (tests):
        print (i+1, end=" ")
        print(getpossibilities(int(input())))

    # UVA 3xN
    global fsol, gsol
    fsol=[-1 for _ in range(maximumN+1)]
    gsol=[-1 for _ in range(maximumN+1)]

    #3 init variables for n-2
    fsol[0] = 0
    fsol[1] = 0
    fsol[2] =3

    gsol[0] = 0
    gsol[1] =1

    n = int(input())
    while n!= -1:
        print (1) if n==0 else print(f(n))
        n= int(input())

# SPOJ 4xN
def getpossibilities(n):
    if n < 0:
        return 0
    if solution[n] != -1:
        return solution[n]
    else:
        out = getpossibilities(n - 1) + 5 * getpossibilities(n - 2) + getpossibilities(n - 3) - getpossibilities(n - 4)
        solution[n] = out
        return out

# UVA 3xN
def f(n):
    if fsol [n] != -1:
        return fsol[n]
    else:
        out = f(n-2) + 2*g(n-1)
        fsol[n]= out
        return out
def g(n):
    if gsol [n]!=-1:
        return gsol[n]
    else:
        out = f(n-1) + g(n-2)
        gsol[n] = out
        return out

readinput()