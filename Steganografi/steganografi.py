import numpy as np
import matplotlib.pyplot as plt
import cv2

res = cv2.imread('cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
sifreli = np.zeros((m, n), dtype=np.int_)
metin = 'Adli Bilisim Mühendisligi'
binary = list()
for i in metin:
    binary.append(np.binary_repr(ord(i), width=8))
binary[:] = [''.join((binary[:]))]
binary = binary[0]
sayac = 0

for i in range(m):
    for j in range(n):
        if len(binary) != int(sayac):
            if res[i, j] % 2 == 0:
                sifreli[i, j] = res[i, j] + int(binary[sayac])
            else:
                sifreli[i, j] = res[i, j] - 1
                sifreli[i, j] = res[i, j] + int(binary[sayac])
            sayac += 1
        else:
            sifreli[i, j] = res[i, j]

print("N =", res[0:1, 0:200], "\nS =", sifreli[0:1, 0:200])
plt.subplot(1, 2, 1), plt.imshow(res, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Orjinal Resim')
plt.subplot(1, 2, 2), plt.imshow(sifreli, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.title('Şifreli Resim')
plt.show()
