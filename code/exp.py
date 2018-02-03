import matplotlib.pyplot as plt
import pickle

execfile("test.py")

n = range(0, 50, 2)
prob = range(15, 90, 15)


t = pickle.load(open("time.p", "rb"))
num = pickle.load(open("num.p", "rb"))
ln = pickle.load(open("leng.p", "rb"))

plt.figure(1)
for i in range(len(prob)):
    plt.plot(n, [item[i] for item in t])

plt.xlabel('n vertici')
plt.ylabel('tempo')

plt.title('Tempo di calcolo di SCC')
plt.legend(['15%', '30%', '45%', '60%', '75%'])

plt.figure(2)
for i in range(len(prob)):
    plt.plot(n, [item[i] for item in num])

plt.xlabel('n vertici')
plt.ylabel('n SCC')

plt.title('Numero di SCC')
plt.legend(['15%', '30%', '45%', '60%', '75%'])

plt.figure(3)
for i in range(len(prob)):
    plt.plot(n, [item[i] for item in ln])

plt.xlabel('n vertici')
plt.ylabel('len di SCC')

plt.title('Lunghezza media di SCC')
plt.legend(['15%', '30%', '45%', '60%', '75%'])


plt.show()








