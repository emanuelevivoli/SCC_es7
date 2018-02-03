# coding=utf-8
import random
import pickle
import numpy

class V:
    def __init__(self, key):
        self.key = key
        self.color = None
        self.p = None
        self.d = None
        self.f = None

    def printV(self):
        print("V: "+str(self.key)+" | "+str(self.color)+" | p:"+str(None if self.p is None else self.p.key)+" ( "+str(self.d)+","+str(self.f)+")")

class G:

    def __init__(self, n, prob):
        self.SCC = []
        self.tree = []                                                  #ALBERO DF GENERATO AD OGNI DFS_VISIT
        self.V = []
        self.temp = []
        self.time = 0

        #create a group of Summit
        for i in range (n):
            self.V.append( V(i))

        #create matrix |n| X |n| of 0
        self.E = [[0 for i in range (n)]for j in range (n)]
        for i in range (n):
            for j in range (n):
                    #set 1 with probability 'prob', 0 with '1-prob'
                    if random.randint(1,100) <= prob:
                        self.E[i][j] = 1
                    else:
                        self.E[i][j] = 0

    def printE(self):
        for i in range(len(self.E)):
            print(self.E[i])
        print

    def printV(self):
        print
        for i in range(len(self.V)):
            self.V[i].printV()



def DFS(G):
    G.SCC = []
    G.temp = []                                                      # resetto temp

    for u in G.V:
        u.color = "w"
        u.p = None
    G.time = 0
    for u in G.V:
        if u.color == 'w':
            G.tree = []
            DFS_visit(G, u)
            G.SCC.append(G.tree)

    # metto in vertici l'elenco in ordine decrescente di tempo finale contenuto in temp
    G.V = G.temp


def DFS_visit(G, u):
    G.time += 1
    u.d = G.time
    u.color= 'g'
    for v in G.V:                                              #v indica i vertici nel vettore di vertici
        if G.E[u.key][v.key] == 1:                                     #se il vertice v è raggiungibile dal vertice u
            if v.color == 'w':
                v.p = u
                DFS_visit(G, v)

    u.color = 'b'
    G.time += 1
    u.f = G.time
    G.temp.insert(0, u)
    G.tree.insert(0, u)


def SCC(G):
    DFS(G)                                  #PRIMA DFS
    G.E = numpy.transpose(G.E)
    DFS(G)                                  #SECONDA DFS SULLA TRASPOSTA
    G.E = numpy.transpose(G.E)


def test(n, prob):
    g = G(n, prob)
    g.printE()

    print
    SCC(g)

    print
    g.printV()

    print
    for i in range(len(g.SCC)):
        print
        for j in range(len(g.SCC[i])):
            print(str(g.SCC[i][j].key)+" ")


#test(100, 3)




