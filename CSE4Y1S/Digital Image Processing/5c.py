# Take a binary image and a structuring element to perform the following morphological operations – 
#5(c) Boundary extraction using morphological operation 
# img-erosion(img)

import cv2
import numpy as np
import matplotlib.pyplot as plt

def erosion_operation(img, mask):
    row, col = img.shape
    pad = len(mask) // 2
    temp = np.zeros((row, col))

    for r in range(row):
        for c in range(col):
            cnt = 0
            for i in range(-pad, pad + 1, 1):
                for j in range(-pad, pad + 1, 1):
                    # corresponding images index
                    nr = i + r
                    nc = j + c
                    if (nr >= 0 and nc >= 0 and nr < row and nc < col):  # boundary check
                        if (mask[i + 1][j + 1] == 1 and img[nr][nc] == 1): #mask[i+pad]==mask[i+1]
                            cnt += 1
            if (cnt == 5):  # for 3*3 mask numner of 1 in structuring element
                temp[r][c] = 1
    return temp

def dilation_operation(img, mask):
    row, col = img.shape
    temp = np.zeros((row, col))
    pad = len(mask) // 2

    for r in range(row):
        for c in range(col):
            cnt = 0
            for i in range(-pad, pad + 1, 1):
                for j in range(-pad, pad + 1, 1):
                    nr = i + r
                    nc = j + c
                    if (nr >= 0 and nc >= 0 and nr < row and nc < col):
                        if (mask[i + pad][j + pad] == 1 and img[nr][nc] == 1):
                            cnt = 1
            if (cnt != 0):
                temp[r][c] = 1
    return temp


def main():
    img = cv2.imread('../images/boundary_extraction.png', cv2.IMREAD_GRAYSCALE)
    row, col = 512, 512
    img = cv2.resize(img, (row, col))

    struct_element = [[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]]
    img = img / 256
    img = np.floor(img * 2)
    # img = np.uint8(img)
    
    erosioned_img = erosion_operation(img, struct_element)
    erosioned_img=img-erosioned_img

    plt.subplot(2, 1, 1)
    plt.imshow(img, cmap='gray')
    plt.title('original image')

    plt.subplot(2, 1, 2)
    plt.imshow(erosioned_img, cmap='gray')
    plt.title('Boundary Exgraction')
    

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
