import numpy as np
import cv2
import matplotlib.pyplot as plt


def histogram(resim):
    x = np.arange(0, 256)
    histo = np.zeros(256)
    res = resim
    m, n = res.shape[:2]
    for i in range(m):
        for j in range(n):
            histo[res[i][j] + 1] += 1
    return x, histo



resim = cv2.imread('cameraman.tif',cv2.IMREAD_GRAYSCALE)
x, hist = histogram(resim)
plt.plot(x, hist)
plt.show()