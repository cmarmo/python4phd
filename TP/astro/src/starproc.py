import numpy as np
from matplotlib import pyplot as plt

from skyobjects import Star

def main(starlist):

    r = np.zeros(len(starlist))
    g = np.zeros(len(starlist))
    gr = np.zeros(len(starlist))
    for i in range(0,len(starlist)):
        r[i] = starlist[i].mag
        g[i] = starlist[i].gmag
        gr[i] = starlist[i].color

    num_bins = 50

    fig, ax = plt.subplots(1,3,sharey=True)

    ax[0] = plt.subplot(131)
    plt.xlabel('R Magnitude')
    plt.ylabel('Number of stars')
    n, bins, patches = ax[0].hist(r, num_bins, density=1)

    ax[1] = plt.subplot(132)
    plt.xlabel('G Magnitude')
    n, bins, patches = ax[1].hist(g, num_bins, density=1)

    ax[2] = plt.subplot(133)
    plt.xlabel('G-R color')
    #plt.ylabel('Number of stars')
    n, bins, patches = ax[2].hist(gr, num_bins, density=1)

    plt.show()

if __name__ == "__main__":
    main(starlist)

