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
    def __str__(self):
        return str(self.items)

def dfs (graph, r):
    """"Takes graph as a adjectancy list and the root node r"""
    n = len(graph)
    N = [False] * n
    P = [-1] *n
    stack = Stack()
    stack.push(r)
    nodesvisited = 0
    while not stack.is_empty():
        u = stack.pop()
        nodesvisited+=1
        #print (u)
        N[u] = True
        for v in (graph [u]):
            if v != P[u]:
                if N[v] == False :
                    P[v] =u
                    stack.push(v)
                else:
                    return False

    return True if nodesvisited==n else False

def readinput ():
    [n,m] = list(map(int,input().split()))
    graph = [[] * n for _ in range(n)]
    for _ in range(m):
        [PV, KV] = list(map(int, input().split()))
        PV-=1
        KV-=1
        graph[PV].append(KV)
        graph[KV].append(PV)

    if n-1 != m:
        print("NO")
    else:
        print ("YES" if dfs(graph,0) else "NO")
readinput()