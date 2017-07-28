def readinput():
    line = input()
    first = True
    while True:
        n, m = int (line.split()[0]), int (line.split()[1])
        if n ==0 and m ==0:
            break
        graph = [[] * n for i in range(n)]
        for i in range(m):
            s = input().split()
            PV = int(s[0])-1
            KV = int(s[1])-1
            graph[PV].append(KV)

        if not first:
            print()
            Topological(graph)
        else:
            first = False
            Topological(graph)

        line = input()

def Topological (graph):
    n = len(graph)
    N = [False] * n
    Z = []
#FIRST STEP - DFS (graph) and memorizing time of leaving vertexes in Stack Z

    def dfs(r,graph,Z):
        N[r] = True
        for v in graph[r]:
            if not N[v]:
                Z = dfs(v, graph, Z)
            else:
                if Z is None or v not in Z:
                     return None
        Z.append(r)
        return Z

    for i in range(n):
        if not N[i]:
            Vr = dfs(i,graph, [])
            if Vr:
                Z.extend(Vr)
    Z = list(reversed(Z))
    for i in Z:
        print(i + 1, end=" ")



readinput()