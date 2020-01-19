import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]

histo, indis = np.histogram(res.ravel(), 256, [0, 256])

h1 = histo[0:127]
h2 = histo[128:255]
t1 = max(h1)
t2 = max(h2)
A, B = np.zeros((2, 2), dtype=np.float), np.zeros((2, 2), dtype=np.float)
w, h = m/2, n/2
yd = np.zeros((int(w), int(h)))
r = 0
for i in range(0, m, 2):
    c = 0
    for j in range(0, n, 2):
        blok = res[i:i + 2, j:j + 2]
        for k in range(2):
            for l in range(2):
                if blok[k, l] <= t1:
                    A[k, l] = blok[k, l] / t1
                    B[k, l] = blok[k, l] / t2
                else:
                    A[k, l] = (255 - blok[k, l]) / (255 - t1)
                    B[k, l] = (255 - blok[k, l]) / (255 - t2)
        yd[r, c] = np.sum(np.sum(np.multiply(np.multiply(blok, A), B)))
        c += 1
    r += 1

plt.subplot(1, 2, 1), plt.imshow(res, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Orijinal')
plt.subplot(1, 2, 2), plt.imshow(yd, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Bulanık Mantık')
plt.show()
