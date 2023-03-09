import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
for line in open('input1.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x.append(int(lines[0]))
    y.append(int(lines[1]))
plt.scatter(x, y, marker='o', c='g')
# plt.show()

a1 = np.random.randint(min(x), max(x))
b1 = np.random.randint(min(y), max(y))

#print("Min x: ", min(x), " Max x: ", max(x), " Random: ", a)
#print("Min y: ", min(y), " Max y: ", max(y), " Random: ", b)

a2 = np.random.randint(min(x), max(x))
b2 = np.random.randint(min(y), max(y))

a3 = np.random.randint(min(x), max(x))
b3 = np.random.randint(min(y), max(y))
#print("Centroid 1: ", a1, ",", b1)
#print("Centroid 2: ", a2, ",", b2)
#print("Centroid 3: ", a3, ",", b3)
