import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import *


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def closest_node(tree, p):
    dist_list = []
    for i in range(0, len(tree)):
        dist_list.append(dist(tree[i], p))
    min_index = dist_list.index(min(dist_list))
    return tree[min_index]


def rrt(start, goal):
    tree = []
    parent = {}
    eqn = {}
    count = 0
    count1 = 0
    X = [start[0]]
    Y = [start[1]]
    lim_iterate = int(input("Enter the no. of iterations: "))
    tree.append(start)
    while count != lim_iterate:
        xr = random.uniform(-40, 40)
        yr = random.uniform(-40, 40)
        x_, y_ = closest_node(tree, (xr, yr))

        if xr != x_:
            theta = math.atan((yr - y_) / (xr - x_))
            m = (yr - y_) / (xr - x_)

            if theta < 0:
                theta += np.pi

            if yr - y_ >= 0:
                x = (x_ + 0.5*math.cos(theta))
                y = (y_ + 0.5*math.sin(theta))
            else:
                x = (x_ - 0.5*math.cos(theta))
                y = (y_ - 0.5*math.sin(theta))

            if goal[1] == m*(goal[0] - x_) + y_:
                parent[(goal[0], goal[1])] = (x_, y_)
                count1 = 1
                break
            else:
                t = linspace(min(x, x_), max(x, x_), 200)
                a = m * (t - x_) + y_
                tree.append((x, y))
                eqn[count] = (t, a)
                parent[(x, y)] = (x_, y_)
                count += 1

    plt.xlim((-40, 40))
    plt.ylim((-40, 40))

    plt.plot(X, Y, marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")

    for i in range(len(eqn)):
        plt.plot(eqn[i][0], eqn[i][1], 'b')
    plt.show()

    if count1 == 1:
        xc, yc = goal
        while xc != start[0] and yc != start[1]:
            x_values = [xc, parent[(xc, yc)][0]]
            y_values = [yc, parent[(xc, yc)][1]]
            plt.plot(x_values, y_values, 'bo', linestyle="--")
            xc, yc = parent[(xc, yc)]
        plt.show()

    return


Start = (0, 0)
Goal = (7., 19.)
rrt(Start, Goal)
