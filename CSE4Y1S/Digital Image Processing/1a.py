#Take grayscale image of size 512x512 and perform the following operations - 

# Decrease its spatial resolution by half every time and observe its change when displaying in the same window size

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('../images/rose.jpg', cv2.IMREAD_GRAYSCALE)
    width = 512
    height = 512
    img = cv2.resize(img, (height, width))
    
    n = 7
    img_list = []
    img_list.append(img)

    for i in range(n):
        h, w = img.shape
        tmp_img = np.zeros((h // 2, w // 2))
        for i in range(0, h // 2):
            for j in range(0, w // 2):
                tmp_img[i, j] = img[i * 2, j * 2]

        img_list.append(tmp_img)
        img = tmp_img

    length = len(img_list)

    for i in range(length):
        plt.subplot(3, 3, i + 1)
        plt.imshow(img_list[i], cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
