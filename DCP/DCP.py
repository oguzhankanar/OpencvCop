import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
p, q = np.zeros(8), np.zeros(8)
tek, cift = np.zeros((m, n)), np.zeros((m, n))
for i in range(m - 4):
    for j in range(n - 4):
        blok = res[i:i + 5, j:j + 5]
        pc, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7] = blok[2, 2], blok[1, 2], blok[1, 3], blok[2, 3], blok[3, 3], \
                                                             blok[3, 2], blok[3, 1], blok[2, 1], blok[1, 1]
        q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7] = blok[0, 2], blok[0, 4], blok[2, 4], blok[4, 4], blok[4, 2], \
                                                         blok[4, 0], blok[2, 0], blok[0, 0]

        for k in range(8):
            dcp = np.zeros(8)
            dcp[k] = int(p[k] >= pc) * 2 + int(q[k] >= p[k])
        say = 1
        for k in range(0, 8, 2):
            tek[i, j] += dcp[k] * 4 ** (4 - say)
            cift[i, j] += dcp[k + 1] * 4 ** (4 - say)
            say += 1
h1, h2 = np.histogram(tek.ravel(), 256, [0, 256])
print(h2)
h2, x = np.histogram(cift.ravel(), 256, [0, 256])
hist = np.append(np.transpose(h1), np.transpose(h2))
hist = np.transpose(hist)

plt.subplot(2, 3, 1), plt.imshow(tek, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('TEK')
plt.subplot(2, 3, 2), plt.imshow(cift, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('ÇİFT')
plt.subplot(2, 3, 3), plt.plot(h1), plt.title('TEK HİSTOGRAM')
plt.subplot(2, 3, 4), plt.plot(h2), plt.title('ÇİFT HİSTOGRAM')
plt.subplot(2, 3, 5), plt.plot(hist), plt.title('512 ÖZELLİK')
plt.show()
