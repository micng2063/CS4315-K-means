import matplotlib.pyplot as plt
import numpy as np
import math

x = []
y = []
for line in open('input1.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x.append(int(lines[0]))
    y.append(int(lines[1]))
#plt.scatter(x, y, marker='o', c='g')
# plt.show()
#print("Min x: ", min(x), " Max x: ", max(x), " Random: ", a)
#print("Min y: ", min(y), " Max y: ", max(y), " Random: ", b)
#print("Centroid 1: ", a1, ",", b1)
#print("Centroid 2: ", a2, ",", b2)
#print("Centroid 3: ", a3, ",", b3)

a1 = np.random.randint(min(x), max(x))
b1 = np.random.randint(min(y), max(y))

a2 = np.random.randint(min(x), max(x))
b2 = np.random.randint(min(y), max(y))

a3 = np.random.randint(min(x), max(x))
b3 = np.random.randint(min(y), max(y))

print("centroid 1:" , a1, " , ", b1)
print("centroid 2:" , a2, " , ", b2)
print("centroid 3:" , a3, " , ", b3)

z  = []
i = 0
label = 0
while i in range (len(x)):
    d1 = math.dist([x[i],y[i]], [a1,b1])
    d2 = math.dist([x[i],y[i]], [a2,b2])
    d3 = math.dist([x[i],y[i]], [a3,b3])
    if d1 == min(d1,d2,d3):
        label = 1
    elif d2 == min(d1,d2,d3):
        label = 2
    elif d3 == min(d1, d2, d3):
        label = 3
    z.append(label)

    print("xy:" , x[i], ",", y[i], " || d1: ", round(d1, 3), "d2: ", round(d2, 3), " d3: ", round(d3, 3), " label: ", z[i])
    i += 1
