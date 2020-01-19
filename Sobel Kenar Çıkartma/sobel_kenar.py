import cv2
import numpy as np
import matplotlib.pyplot as plt

mx = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
my = mx.transpose()
res = cv2.imread('/home/scorp/cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
kenar = np.zeros((m, n))

edge = cv2.Laplacian(res, cv2.CV_64F)

for i in range(m - 2):
    for j in range(n - 2):
        gx = np.sum(np.sum(np.multiply(res[i:i + 3, j:j + 3], mx)))
        gy = np.sum(np.sum(np.multiply(res[i:i + 3, j:j + 3], mx)))
        G = np.sqrt(gx ** 2 + gy ** 2)
        if G > 255:
            kenar[i, j] = 1
        else:
            kenar[i, j] = 0
plt.subplot(2, 2, 1), plt.imshow(kenar, cmap='gray'), plt.title("Kod Çıktısı")
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(edge, cmap='gray'), plt.title("Hazır Fonks")
plt.xticks([]), plt.yticks([])
plt.show()
