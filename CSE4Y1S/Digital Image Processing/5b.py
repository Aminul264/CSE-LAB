# Take a binary image and a structuring element to perform the following morphological operations – 
#5(b) Opening and Closing operationsn 
# for opening
# img1=erosion(img)
# img=dilation(img1)

# for dilation
# img1=dilation(img)
# img=erosion(img1)

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
                    nr = i + r
                    nc = j + c

                    if (nr >= 0 and nc >= 0 and nr < row and nc < col):
                        if (mask[i + pad][j + pad] == 1 and img[nr][nc] == 1):
                            cnt += 1
            if (cnt == 9):  # given 3*3 mask -> no. of 1=9
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

def opening_operation(img, structuring_element):
    tmp = erosion_operation(img, structuring_element)
    out_img = dilation_operation(tmp, structuring_element)

    return out_img

def closing_operation(img,structuring_element):
    temp=dilation_operation(img,structuring_element)
    out_img=opening_operation(temp,structuring_element)
    
    return out_img
    
def main():
    img = cv2.imread('../images/fingerprint1.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (512, 512))

    # converting into binary image
    img = img / 256
    img = np.floor(img * 2)

    structuring_element = [[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]]

    open_img = opening_operation(img, structuring_element)
    closed_img=closing_operation(img,structuring_element)
    

    plt.subplot(3, 1, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(3, 1, 2)
    plt.imshow(open_img, cmap='gray')
    plt.title('After Opening Operation')
    
    plt.subplot(3, 1, 3)
    plt.imshow(closed_img, cmap='gray')
    plt.title('After Closing Operation')
    
    
    

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
