import matplotlib.pyplot as plt

fig, ax = plt.subplots(4)
x1 = []
y1 = []
for line in open('input1.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x1.append(int(lines[0]))
    y1.append(int(lines[1]))
ax[0].scatter(x1, y1, marker='o', c='g')


x2 = []
y2 = []
for line in open('input2.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x2.append(int(lines[0]))
    y2.append(int(lines[1]))
ax[1].scatter(x2, y2, marker='o', c='r')

x3 = []
y3 = []
for line in open('input3.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x3.append(int(lines[0]))
    y3.append(int(lines[1]))
ax[2].scatter(x3, y3, marker='o', c='b')


x4 = []
y4 = []
for line in open('input3.txt', 'r'):
    lines = [i for i in line.split("\t")]
    x3.append(int(lines[0]))
    y3.append(int(lines[1]))
ax[3].scatter(x3, y3, marker='o', c='yellow')

plt.show()
