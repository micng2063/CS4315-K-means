import matplotlib.pyplot as plt
import numpy as np
import math

inFile = input("Enter text file: ")
k = int(input("Enter value of k: "))
x = []
y = []
for line in open(inFile, 'r'):
    lines = [i for i in line.split("\t")]
    x.append(int(lines[0]))
    y.append(int(lines[1]))


a1 = np.random.randint(min(x), max(x))
b1 = np.random.randint(min(y), max(y))
a2 = np.random.randint(min(x), max(x))
b2 = np.random.randint(min(y), max(y))
if k >= 3:
    a3 = np.random.randint(min(x), max(x))
    b3 = np.random.randint(min(y), max(y))
    if k == 4:
        a4 = np.random.randint(min(x), max(x))
        b4 = np.random.randint(min(y), max(y))

repeat = 0
repeatRange = 10
if k == 2:
    while repeat in range(repeatRange):
        z = []
        index, label = 0, 0
        while index in range(len(x)):
            d1 = math.dist([x[index], y[index]], [a1, b1])
            d2 = math.dist([x[index], y[index]], [a2, b2])
            if d1 == min(d1, d2):
                label = 1
            elif d2 == min(d1, d2):
                label = 2
            z.append(label)
            index += 1

        label1 = []
        label2 = []

        index = 0
        while index in range(len(z)):
            if z[index] == 1:
                label1.append(index)
            elif z[index] == 2:
                label2.append(index)
            index += 1

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label1)):
            xSum += x[label1[index]]
            ySum += y[label1[index]]
            index += 1
        a1, b1 = xSum / len(label1), ySum / len(label1)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label2)):
            xSum += x[label2[index]]
            ySum += y[label2[index]]
            index += 1
        a2, b2 = xSum / len(label2), ySum / len(label2)

        repeat += 1
        if repeat == (repeatRange-1):
            print("Centroid 1: ", round(a1,3), ",", round(b1,3))
            print("Centroid 2: ", round(a2,3), ",", round(b2,3))
            print("Label:", z)
        if repeat < repeatRange:
            z.clear()
if k == 3:
    while repeat in range(repeatRange):
        z = []
        index, label = 0, 0
        while index in range(len(x)):
            d1 = math.dist([x[index], y[index]], [a1, b1])
            d2 = math.dist([x[index], y[index]], [a2, b2])
            d3 = math.dist([x[index], y[index]], [a3, b3])
            if d1 == min(d1, d2, d3):
                label = 1
            elif d2 == min(d1, d2, d3):
                label = 2
            elif d3 == min(d1, d2, d3):
                label = 3
            z.append(label)
            index += 1

        label1 = []
        label2 = []
        label3 = []

        index = 0
        while index in range(len(z)):
            if z[index] == 1:
                label1.append(index)
            elif z[index] == 2:
                label2.append(index)
            elif z[index] == 3:
                label3.append(index)
            index += 1

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label1)):
            xSum += x[label1[index]]
            ySum += y[label1[index]]
            index += 1
        a1, b1 = xSum / len(label1), ySum / len(label1)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label2)):
            xSum += x[label2[index]]
            ySum += y[label2[index]]
            index += 1
        a2, b2 = xSum / len(label2), ySum / len(label2)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label3)):
            xSum += x[label3[index]]
            ySum += y[label3[index]]
            index += 1
        a3, b3 = xSum / len(label3), ySum / len(label3)

        repeat += 1
        if repeat == (repeatRange-1):
            print("Centroid 1: ", round(a1,3), ",", round(b1,3))
            print("Centroid 2: ", round(a2,3), ",", round(b2,3))
            print("Centroid 3: ", round(a3,3), ",", round(b3,3))
            print("Label:", z)
        if repeat < repeatRange:
            z.clear()
elif k == 4:
    while repeat in range(repeatRange):
        z = []
        index, label = 0, 0
        while index in range(len(x)):
            d1 = math.dist([x[index], y[index]], [a1, b1])
            d2 = math.dist([x[index], y[index]], [a2, b2])
            d3 = math.dist([x[index], y[index]], [a3, b3])
            d4 = math.dist([x[index], y[index]], [a4, b4])
            if d1 == min(d1, d2, d3, d4):
                label = 1
            elif d2 == min(d1, d2, d3, d4):
                label = 2
            elif d3 == min(d1, d2, d3, d4):
                label = 3
            elif d4 == min(d1, d2, d3, d4):
                label = 4
            z.append(label)
            index += 1

        label1 = []
        label2 = []
        label3 = []
        label4 = []

        index = 0
        while index in range(len(z)):
            if z[index] == 1:
                label1.append(index)
            elif z[index] == 2:
                label2.append(index)
            elif z[index] == 3:
                label3.append(index)
            elif z[index] == 4:
                label4.append(index)
            index += 1

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label1)):
            xSum += x[label1[index]]
            ySum += y[label1[index]]
            index += 1
        a1, b1 = xSum / len(label1), ySum / len(label1)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label2)):
            xSum += x[label2[index]]
            ySum += y[label2[index]]
            index += 1
        a2, b2 = xSum / len(label2), ySum / len(label2)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label3)):
            xSum += x[label3[index]]
            ySum += y[label3[index]]
            index += 1
        a3, b3 = xSum / len(label3), ySum / len(label3)

        index, xSum, ySum = 0, 0, 0
        while index in range(len(label4)):
            xSum += x[label4[index]]
            ySum += y[label4[index]]
            index += 1
        a4, b4 = xSum / len(label4), ySum / len(label4)

        repeat += 1
        if repeat == (repeatRange-1):
            print("Centroid 1: ", round(a1,3), ",", round(b1,3))
            print("Centroid 2: ", round(a2,3), ",", round(b2,3))
            print("Centroid 3: ", round(a3,3), ",", round(b3,3))
            print("Centroid 4: ", round(a4,3), ",", round(b4,3))
            print("Label:", z)
        if repeat < repeatRange:
            z.clear()

file1 = open("output.txt","w")
index = 0
text = ""
while index in range (len(x)):
    text = str(x[index]) + "\t" + str(y[index]) + "\t" + str(z[index]) +"\n"
    file1.write(text)
    index +=1
file1.close()