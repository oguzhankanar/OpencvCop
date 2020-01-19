import cv2
import numpy as np
import matplotlib.pyplot as plt

gri = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = gri.shape[:2]
sb = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        if gri[i, j] >= 150:
            sb[i, j] = 1
        else:
            sb[i, j] = 0
plt.subplot(1, 2, 2), plt.imshow(sb, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Siyah Beyaz')
plt.subplot(1, 2, 1), plt.imshow(gri, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Gri Resim')
plt.show()
