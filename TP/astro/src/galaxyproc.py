import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse

from skyobjects import Galaxy

def main(galaxylist):
    num = len(galaxylist)

    ra = np.zeros(num)
    dec = np.zeros(num)
    rad = np.zeros(num)
    ells = []
    for i in range(0,num):
        ra[i] = galaxylist[i].ra
        dec[i] = galaxylist[i].dec
        rad[i] = galaxylist[i].dVrad / 1800.
        ells.append(Ellipse(xy=(ra[i],dec[i]), width=rad[i],
                            height=rad[i]*galaxylist[i].dVell,
                            angle=galaxylist[i].PA))

    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

    for e in ells:
        ax.add_artist(e)
        e.set_clip_box(ax.bbox)
        e.set_alpha(np.random.rand())
        e.set_facecolor(np.random.rand(3))

    ax.set_xlim(ra.min(), ra.max())
    ax.set_ylim(dec.min(), dec.max())
    plt.show()

if __name__ == "__main__":
    main(galaxylist)

