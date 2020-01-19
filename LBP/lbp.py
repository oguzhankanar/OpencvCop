import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
yeni = np.zeros((256, 256))
m, n = res.shape[:2]
for i in range(0, m - 2):
    for j in range(0, n - 2):
        p = res[i:i + 3, j:j + 3]
        pc = p[1, 1]
        yeni[i, j] = 0
        sayac = 1
        for k in range(0, 3):
            for l in range(0, 3):
                if k != 1 and l != 1:
                    yeni[i, j] = yeni[i, j] + int(p[k, l] >= pc) * (2 ** (8 - sayac))
                    sayac += 1
plt.subplot(1, 2, 1), plt.imshow(res, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Gri Resim')
plt.subplot(1, 2, 2), plt.imshow(yeni, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Yeni Resim')
plt.show()
