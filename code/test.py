import Graph as Grafo
from timeit import default_timer as time
import pickle

n = range(0, 50, 2)
prob = range(15, 90, 15)

t = [[] for i in n]
num = [[] for i in n]
ln = [[] for i in n]



for i in range(len(n)):

    t[i] = [0 for j in range(len(prob))]
    num[i] = [0 for j in range(len(prob))]
    ln[i] = [0 for j in range(len(prob))]

    for j in range(len(prob)):
        for k in range(20):

            g = Grafo.G(n[i], prob[j])
            start = time()
            Grafo.SCC(g)
            end = time()

            len_m = 0
            for l in range(len(g.SCC)):
                len_m += len(g.SCC[l])
            len_m /= (1 if len(g.SCC) == 0 else len(g.SCC))


            t[i][j] = (t[i][j] * k + (end - start)) / (k + 1)
            num[i][j] = (num[i][j] * k + len(g.SCC)) / (k + 1)
            ln[i][j] = (ln[i][j] * k + len_m) / (k + 1)


pickle.dump(t, open("time.p", "wb"))
pickle.dump(num, open("num.p", "wb"))
pickle.dump(ln, open("leng.p", "wb"))