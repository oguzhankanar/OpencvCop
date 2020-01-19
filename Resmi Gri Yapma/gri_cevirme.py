import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif')
w, h, z = res.shape
gri = np.zeros((w, h))
for i in range(w):
    for j in range(h):
        for k in range(z):
            toplam = 0
            toplam += res[i, j, k]
        gri[i, j] = int(toplam / 4)

plt.subplot(1, 2, 2), plt.imshow(gri, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Gri Resim')
plt.subplot(1, 2, 1), plt.imshow(res), plt.xticks([]), plt.yticks([]), plt.title('Orjinal Resim')
plt.show()