# Vertice
class V:
    def __init__(self, key):
        self.key = key
        self.color = None
        self.p = None
        self.d = None
        self.f = None


# Graph
class G:

    def __init__(self, n, prob):
        self.SCC = []
        self.V = []
        self.time = 0

        # create a group of Summit
        for i in range(n):
            self.V.append(V(i))

        # create matrix |n| x |n| of 0
        self.E = [[0 for i in range(n)]
                        for j in range(n)]
        for i in range(n):
            for j in range(n):
                    # set   1 with probability 'prob'
                    #       0 with probability '1-prob'
                    if random.randint(1, 100) <= prob:
                        self.E[i][j] = 1
                    else:
                        self.E[i][j] = 0