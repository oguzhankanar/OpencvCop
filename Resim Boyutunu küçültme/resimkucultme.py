import cv2
import numpy as np
import matplotlib.pyplot as plt

orj = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = orj.shape[:2]
yeni = np.zeros((int(m/2), int(n/2)), dtype=np.float_)
satir = 0
for i in range(0, m-1, 2):
    sutun = 0
    for j in range(0, n-1, 2):
        yeni[satir, sutun] = int(np.sum(np.sum(orj[i:i+2, j:j+2]))/4)
        sutun += 1
    satir += 1
plt.subplot(1, 2, 1), plt.imshow(yeni, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Yeni Resim')
plt.subplot(1, 2, 2), plt.imshow(orj, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Eski Resim')
plt.show()