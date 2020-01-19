import cv2
import numpy as np
import matplotlib.pyplot as plt
# 256 x 256 Boyutundaki görüntüyü 512 x 512 boyutuna çevirir
res = cv2.imread('/home/scorp/cameraman.tif', cv2.IMREAD_GRAYSCALE)
m, n = res.shape[:2]
yeni = np.zeros((512, 512))
satir = 0
for i in range(m):
    sutun = 0
    for j in range(n):
        yeni[satir: satir + 2, sutun: sutun + 2] = int(res[i, j])
        sutun += 2
    satir += 2
figure, (axs1, axs2) = plt.subplots(1, 2)
figure.suptitle('RESİMLER')
axs1.imshow(res,cmap='gray')
axs1.set_title('Eski Resim')
axs2.imshow(yeni,cmap='gray')
axs2.set_title('Yeni Resim')
plt.show()
