import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
(tresh, sb) = cv2.threshold(res, 150, 1, cv2.THRESH_BINARY)  # Siyah beyaza çeviren otomatik fonksyon
m, n = res.shape[:2]
kenar = np.zeros((m, n))
for i in range(m - 1):
    for j in range(n - 1):
        tpl = np.sum(np.sum(sb[i:i + 2, j:j + 2]))
        if tpl == 0 or tpl == 4:
            kenar[i, j] = 0
        else:
            kenar[i, j] = 1
plt.subplot(1, 3, 1), plt.imshow(res, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Orjinal')
plt.subplot(1, 3, 2), plt.imshow(kenar, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Kenar')
plt.subplot(1, 3, 3), plt.imshow(sb, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('S&B')
plt.show()
