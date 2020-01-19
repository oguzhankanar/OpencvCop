#dörtlü pattern 
import cv2
import numpy as np
import matplotlib.pyplot as plt
res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
esik = 5
p = np.zeros((3, 3))
bl = np.zeros(8)
bu = np.zeros(8)
upper = np.zeros((m, n))
lower = np.zeros((m, n))
for i in range(m-2):
    for j in range(n-2):
        p = res[i:i + 3, j: j + 3]
        pc = p[1, 1]
        sayac = 0
        fark = np.zeros(8)
        for k in range(3):
            for l in range(3):
                if k != 1 or l != 1:
                    fark[sayac] = p[k, l] - pc
                    sayac += 1
        for k in range(8):
            if fark[k] < esik:
                bl[k], bu[k] = 1, 0
            elif fark[k] >= esik >= fark[k]:
                bl[k], bu[k] = 0, 0
            else:
                bl[k], bu[k] = 0, 1
            upper[i][j] = upper[i][j] + bu[k]*(2**(8-k))
            lower[i][j] = lower[i][j] + bl[k]*(2**(8-k))

lhist, deger = np.histogram(lower.ravel(), 256, [0, 256])
del deger
uhist, deger = np.histogram(lower.ravel(), 256, [0, 256])
del deger

plt.subplot(2, 2, 1), plt.plot(lhist), plt.title('Lower Histogram')
plt.subplot(2, 2, 2), plt.plot(uhist), plt.title('Upper Histogram')
plt.subplot(2, 2, 3), plt.imshow(lower, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Lower')
plt.subplot(2, 2, 4), plt.imshow(upper, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Upper')
plt.show()