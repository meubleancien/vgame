import random
import matplotlib.pyplot as plt
import numpy as np



#random.seed(10)


def VgameRand(a, b):
    c = random.randint(a,b)
    if c <= random.randint(a,b):
        return c
    else:
        return 0


def VgameStrat(a, b, cH):
    if cH <= random.randint(a,b):
        return cH
    else:
        return 0


def MeanGame(cH1):
    array = np.array([])
    for j in cH1:
        a = 0
        for i in range(100000):
            a += VgameStrat(400, 1600, j)
        array = np.append(array, a/100000)
    return array




### Graph ###


x = np.linspace(600, 1400, 70)

plt.plot(x, MeanGame(x), color='red')

def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

annot_max(x,MeanGame(x))
plt.show()


#next step: better plot and strategy




