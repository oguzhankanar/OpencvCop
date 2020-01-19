import cv2
import numpy as np
import matplotlib.pyplot as plt

res = cv2.imread('/home/scorp/cameraman.tif',cv2.IMREAD_GRAYSCALE)
blok = np.zeros((2, 2))
yeni = np.zeros((256, 256))
yeni1 = np.zeros((256, 256))

for i in range(256):
    for j in range(256):
        yeni[i, j] = np.mean(np.mean(res[i:i+2, j:j+2]))
        yeni1[i, j] = np.median(np.median(res[i:i+2, j:j+2]))
fig, (axs1, axs2) = plt.subplots(1,2)
fig.suptitle('Filtreler')
axs1.set_title('Mean')
plt.xticks([]), plt.yticks([])
axs1.imshow(yeni, cmap='gray')
axs2.set_title('Median')
plt.xticks([]), plt.yticks([])
axs2.imshow(yeni1, cmap='gray')
plt.show()