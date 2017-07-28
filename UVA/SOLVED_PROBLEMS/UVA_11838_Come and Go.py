#ACCEPTED

class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size()==0
    def push(self, item):
        self.items+=[item]
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def remove (self, v):
        self.items.remove(v)
    def __str__(self):
        return str(self.items)


def readinput():
    line = input()
    while True:
        n, m = int (line.split()[0]), int (line.split()[1])
        if n ==0 and m ==0:
            break

        graph = [[] * n for i in range(n)]
        for i in range(m):
            s = input().split()
            PV = int(s[0])-1
            KV = int(s[1])-1
            oneway = int(s[2])
            graph[PV].append(KV)
            if oneway ==2:
                graph[KV].append(PV)

        print(1 if Kosaraju_Sharrir(graph)==1 else 0)
        line = input()



def createGop(graph):
    graphop = [[] for _ in range (len(graph))]
    for u in range (len(graph)):
        for v in graph[u]:
            graphop[v].append(u)
    return graphop

def Kosaraju_Sharrir (graph):
    n = len(graph)
    N = [False] * n
    Z = Stack()

    def dfs(r,graph):
        N[r] = True
        for v in graph[r]:
            if not N[v]:
                dfs(v, graph)
        Z.push(r)


    for i in range(n):
        if not N[i]:
            dfs(i,graph)

    graphop = createGop(graph)

    componentcounter = 0
    N = [False] * n
    while not Z.is_empty():
        if not N[Z.peek()]:
            dfs (Z.peek(), graphop)
            componentcounter+=1
        else:
            Z.pop()
    return componentcounter

readinput()
