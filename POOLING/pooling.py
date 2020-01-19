import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
yeni1 = np.zeros((m-1,n-1))
yeni2 = np.zeros((m-1,n-1))
for i in range(m-1):
    for j in range(n-1):
        blok = res [i:i+2, j:j+2]
        yeni1[i, j] = np.max(blok)   #MAX pooling
        yeni2[i, j] = np.min(blok)   #MIN pooling
plt.subplot(1, 2, 1), plt.imshow(yeni1, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('MAX POOLİNG')
plt.subplot(1, 2, 2), plt.imshow(yeni2, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('MIN POOLİNG')
plt.show()
