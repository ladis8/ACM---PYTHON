from _collections import deque

def bfs (graph):
    n = len(graph)
    visited = [False] * n
    color = [-1] *n
    numofguards =0


    for i in range (n):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            visited[i] = True
            color[i] = 0
            color0,color1 = 1,0

            while len(queue)!=0:
                u = queue.popleft()
                for v in (graph [u]):
                    if visited[v] == False :
                        queue.append(v)
                        visited[v] = True
                        if color[u] ==1:
                            color[v] = 0
                            color0+=1
                        else:
                            color[v] = 1
                            color1+=1
                    else:
                        if color [v]== color[u]:
                            return -1
            numofguards +=min(color1,color0) if color0+color1 !=1 else 1
    return numofguards


def init():
    t = int(input())
    for _ in range(t):
        [n, m] = list(map(int, input().split()))
        graph = [[] * n for _ in range(n)]
        for _ in range(m):
            [PV, KV] = list(map(int, input().split()))
            graph[PV].append(KV)
            graph[KV].append(PV)
        print(bfs(graph))

init()