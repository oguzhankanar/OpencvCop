import numpy as np
import matplotlib.pyplot as plt
import cv2

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
tr = 2
dcpu, dcpl, p, q = np.zeros(8), np.zeros(8), np.zeros(8), np.zeros(8)
teku, ciftu, tekl, ciftl = np.zeros((m, n)), np.zeros((m, n)), np.zeros((m, n)), np.zeros((m, n))
for i in range(m - 4):
    for j in range(n - 4):
        blok = res[i:i + 5, j:j + 5]
        pc, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7] = blok[2, 2], blok[1, 2], blok[1, 3], blok[2, 3], blok[3, 3], \
                                                             blok[3, 2], blok[3, 1], blok[2, 1], blok[1, 1]
        q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7] = blok[0, 2], blok[0, 4], blok[2, 4], blok[4, 4], blok[4, 2], \
                                                         blok[4, 0], blok[2, 0], blok[0, 0]
        for k in range(8):
            fark1 = p[k] - pc
            fark2 = q[k] - p[k]
            dcpu[k] = int(fark1 > tr) * 2 + int(fark2 > tr)
            dcpl[k] = int(fark1 < -tr) * 2 + int(fark2 < -tr)
        say = 1
        for k in range(0, 8, 2):
            teku[i, j] += dcpu[k] * 4 ** (4 - say)
            tekl[i, j] += dcpl[k] * 4 ** (4 - say)
            ciftu[i, j] += dcpu[k] * 4 ** (4 - say)
            ciftl[i, j] += dcpl[k] * 4 ** (4 - say)
            say += 1

h1, x = np.histogram(tekl.ravel(), 256, [0, 256])
h2, x = np.histogram(teku.ravel(), 256, [0, 256])
h3, x = np.histogram(ciftl.ravel(), 256, [0, 256])
h4, x = np.histogram(ciftu.ravel(), 256, [0, 256])
del x
hist = np.append(np.transpose(h1), np.transpose(h2))
hist = np.append(hist, np.transpose(h3))
hist = np.append(hist, np.transpose(h4))
hist = np.transpose(hist)
plt.subplot(3, 3, 1), plt.imshow(tekl, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('LOWER TEK')
plt.subplot(3, 3, 2), plt.imshow(teku, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('UPPER TEK')
plt.subplot(3, 3, 3), plt.imshow(ciftl, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('LOWER ÇİFT')
plt.subplot(3, 3, 4), plt.imshow(ciftu, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('UPPER ÇİFT')
plt.subplot(3, 3, 5), plt.plot(h1), plt.title('H1')
plt.subplot(3, 3, 6), plt.plot(h2), plt.title('H2')
plt.subplot(3, 3, 7), plt.plot(h3), plt.title('H3')
plt.subplot(3, 3, 8), plt.plot(h4), plt.title('H4')
plt.subplot(3, 3, 9), plt.plot(hist), plt.title('ÖZELLİK')
plt.show()




