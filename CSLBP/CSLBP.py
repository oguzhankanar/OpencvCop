import cv2
import numpy as np
import matplotlib.pyplot as plt

p = np.zeros(8)
res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
cslbp = np.zeros((m, n))
for i in range(m - 2):
    for j in range(n - 2):
        blok = res[i:i + 3, j:j + 3]
        p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7] = blok[0, 1], blok[0, 2], blok[1, 2], blok[2, 2], blok[2, 1], \
                                                         blok[2, 0], blok[1, 0], blok[0, 0]
        pc = blok[1, 1]
        for k in range(4):
            cslbp[i, j] += int(p[k] >= p[k + 4]) * 2 ** (k - 1)

plt.imshow(cslbp, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('CSLBP')
plt.show()
