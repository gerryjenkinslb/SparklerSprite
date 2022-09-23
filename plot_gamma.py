import matplotlib.pyplot as plt
import scipy.special as sps
from sparkler import LEN_SAMPLES, G_SCALE, G_SHAPE
import numpy as np

# this will plot the shape of sample, used to get shape and scale
def stats():  # extra code to plot gamma points to find my curve
    print("stats")
    s = LEN_SAMPLES



    count, bins, ignored = plt.hist(s, 50, density=True)

    y = bins ** (G_SHAPE - 1) * (np.exp(-bins / G_SCALE) /
                                 (sps.gamma(G_SHAPE) * G_SCALE ** G_SHAPE))

    plt.plot(bins, y, linewidth=2, color='r')

    plt.show()


if __name__ == '__main__':
    stats()