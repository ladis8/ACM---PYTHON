#TIME LIMIT EXCEEDED ERROR
#JAVA PASSED

import sys
class Node:
    def __init__(self,id):
        self.parent = None
        self.id = id
        self.rank =0

    def __eq__(self, other):
        return True if self.id == other.id else False
    def __str__(self):
        return str(self.id)
    def __hash__(self):
        return hash(self.id)

class DisjointSet:
    def __init__(self, n):
        """"make disjoint set by several singletons in range 0-n"""
        self.nodes = [Node(id) for id in range(n)]

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        rootnodes = []
        out = "{"
        for i in range(1,len(self.nodes)):
            rootNode = self.find(self.nodes[i].id)
            if rootNode not in rootnodes:
                rootnodes.append(rootNode)

        connectednodes = [{rootNode.id} for rootNode in rootnodes]

        for i in range(1, len(self.nodes)):
            index = rootnodes.index(self.find(self.nodes[i].id))
            connectednodes[index].add(self.nodes[i].id)
        out = "{"
        for m in connectednodes:
            out += str(m)
        out +="}"
        return out

    def find (self, v):
            node = self.nodes [v]
            jumps = 0
            while node.parent:
                node = node.parent
                jumps +=1
            if jumps >1:
                self.repair (v, node.id)
            return node


    def union (self,x, y):
        """"merge the two components with id x and y"""
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
        elif xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot
        else:
            yRoot.parent = xRoot
            xRoot.rank = xRoot.rank +1

    def repair (self, v, rootId):
        node = self.nodes[v]
        while node.id != rootId:
            tmp = node.parent
            node.parent = self.nodes [rootId]
            node = tmp
class Edge:
    def __init__(self, PV, KV, weight):
        self.PV = PV
        self.KV = KV
        self.weight = weight

    def __gt__(self, other):
        return True if self.weight > other.weight else False
    def __lt__(self, other):
        return True if self.weight < other.weight else False
    def __ge__(self, other):
        return True if self.weight >= other.weight else False
    def __le__(self, other):
        return True if self.weight <= other.weight else False
    def __str__(self):
        return "(%d,%d) %d"%(self.PV,self.KV, self.weight)

def JarnikPrime(graph):
    """"ALGORITHM THAT TAKES METRICE OF EDGES AS AN INPUT"""
    n = len(graph)
    g = graph[0].copy() #g... array of cheapest edges to first component
    g [0] =0
    S = {0} #S... set of nodes in first component
    price = 0
    while len(S) != n:
        #this do the magic
        weight,v = min((val, idx) for (idx,val) in enumerate(g) if idx not in S)
        S.add(v)
        price +=weight

        for w in range(n):
            if w not in S:
                g[w] = min (graph [v][w], g[w])#if there is cheaper edge cross v add it
    return price

def readinput():
    line = input()
    while True:

        n, m = int (line.split()[0]), int (line.split()[1])
        if n ==0 and m ==0:
            break
        graph = []
        #graph = [[sys.maxsize] * n for j in range(n)]
        total = 0
        for i in range(m):
            s = input().split()
            PV = int(s[0])
            KV = int(s[1])
            weight = int(s[2])
            graph.append(Edge(PV,KV,weight))
            #graph[PV][KV] = weight
            #graph[KV][PV] = weight
            total +=weight

        #print(total - JarnikPrime(graph))
        print(total - Kruskal(graph,n))
        line = input()


def Kruskal(graph, n):
    """"GREEDY ALGORITM THAT TAKES LIST OF EDGES AS AN INPUT"""
    graph = sorted(graph)
    edgecounter = 0
    DS = DisjointSet(n)
    price= 0
    i = 0

    while edgecounter < n-1 and i < len(graph):
        e,u,v = graph [i], graph[i].PV, graph[i].KV
        i+=1
        if DS.find(u) != DS.find(v):
            DS.union(u,v)
            price+=e.weight
            edgecounter+=1
    return price
readinput()




