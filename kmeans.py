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

    #print("xy:" , x[i], ",", y[i], " || d1: ", round(d1, 3), "d2: ", round(d2, 3), " d3: ", round(d3, 3), " label: ", z[i])
    i += 1

label1 = []
label2 = []
label3 = []

n = 0
while n in range (len(z)):
    if z[n] == 1:
        label1.append(n)
    elif z[n] == 2:
        label2.append(n)
    elif z[n] == 3:
        label3.append(n)
    n+=1

#xy-cordinate index of each cluster
print(label1)
print(label2)
print(label3)

indexLabel1 = 0
xSum1 = 0
ySum1 = 0
while indexLabel1 in range (len(label1)):
    xSum1 += x[label1[indexLabel1]]
    ySum1 += y[label1[indexLabel1]]
    #print("xy:", x[label1[indexLabel1]], ",", y[label1[indexLabel1]])
    indexLabel1 += 1

xCentroid1 = xSum1/len(label1)
yCentroid1 = ySum1/len(label1)
print(xCentroid1, ",", yCentroid1)

indexLabel2 = 0
xSum2 = 0
ySum2 = 0
while indexLabel2 in range (len(label2)):
    xSum2 += x[label2[indexLabel2]]
    ySum2 += y[label2[indexLabel2]]
    #print("xy:", x[label2[indexLabel2]], ",", y[label2[indexLabel2]])
    indexLabel2 += 1

xCentroid2 = xSum2/len(label2)
yCentroid2 = ySum2/len(label2)
print(xCentroid2, ",", yCentroid2)

indexLabel3 = 0
xSum3 = 0
ySum3 = 0
while indexLabel3 in range (len(label3)):
    xSum3 += x[label3[indexLabel3]]
    ySum3 += y[label3[indexLabel3]]
    #print("xy:", x[label3[indexLabel3]], ",", y[label3[indexLabel3]])
    indexLabel3 += 1

xCentroid3 = xSum3/len(label3)
yCentroid3 = ySum3/len(label3)
print(xCentroid3, ",", yCentroid3)

centroid  = []
index = 0
labelCentroid = 0
while index in range (len(x)):
    d1 = math.dist([x[index],y[index]], [xCentroid1,yCentroid1])
    d2 = math.dist([x[index],y[index]], [xCentroid2,yCentroid2])
    d3 = math.dist([x[index],y[index]], [xCentroid3,yCentroid3])
    if d1 == min(d1, d2, d3):
        labelCentroid = 1
    elif d2 == min(d1, d2, d3):
        labelCentroid = 2
    elif d3 == min(d1, d2, d3):
        labelCentroid = 3

    print("label: ", labelCentroid)
    index +=1