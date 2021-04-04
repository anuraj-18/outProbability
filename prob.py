import numpy as np
import matplotlib.pyplot as plt

x=[np.random.randint(0,60) for i in range(100)]
y = [np.random.randint(0,120) for i in range(75)]
x=x+y
np.mean(x),np.std(x)

maxS = max(x)
minS = 0
L = len(x)
buckets = np.zeros((maxS)//3+1)
for i in range(L):
    buckets[x[i]//3] += 1
y=buckets
s=np.arange(len(buckets))

plt.plot(s, y)
plt.show()
