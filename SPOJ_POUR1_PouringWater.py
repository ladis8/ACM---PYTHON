from sys import stdin
from collections import deque

maxa= maxb=goal=-1


""""--------------------VERSION FOR SPOJ SITUATED PROBLEM--------------------"""
#fucking concetration on time


def doBFS ():
    queue = deque()
    queue.append([(0,0),0])
    visited = set()
    count = 0

    while len(queue) !=0:
        [(a,b),depth] = queue.popleft()

        if (a,b) not in visited:
            visited.add((a,b))
            if a == goal or b == goal:
                print(depth)
                break

            m1 = min(maxa, a+b)
            m2 = min (maxb, a+b)

            for n in [(0, b), (a, 0),(maxa, b),(a, maxb),(m1, b-(m1-a)),(a-(m2-b),m2)]:
                if n not in visited and n != (a,b):
                    queue.append([n, depth+1])

        if (len(queue)==0):
            print("-1")



def init ():
    t = int (stdin.readline())
    for _ in range(t):
        try:
            global maxa, maxb,goal
            maxa = int (stdin.readline())
            maxb = int(stdin.readline())
            goal = int(stdin.readline())
            if goal > max(maxa, maxb) or (max(maxa, maxb)%min(maxa, maxb) ==0 and goal%min(maxa, maxb) !=0):
                print("-1")
            else:
                doBFS()

        except EOFError:
            break

init()