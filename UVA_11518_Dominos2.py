N = []
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


def dfs (graph, r):
    """"Takes graph as a adjectancy list and the root node r"""
    global N
    n = len(graph)
    stack = Stack()
    stack.push(r)
    nodesvisited = 1 if N[r] == False else 0
    N[r] = True


    while not stack.is_empty():
        u = stack.pop()
        for v in (graph [u]):
            if N[v] == False :
                nodesvisited+=1
                stack.push(v)
                N[v] = True
    return nodesvisited


def init():
    t = int(input())
    for _ in range(t):
        [n, m,l] = list(map(int, input().split()))
        graph = [[] * n for _ in range(n)]
        for _ in range(m):
            [PV, KV] = list(map(int, input().split()))
            PV -= 1
            KV -= 1
            graph[PV].append(KV)
        out = 0
        global N
        N = [False] * n
        for _ in range(l):
            out+=dfs(graph, int(input())-1)
        print(out)

init()
