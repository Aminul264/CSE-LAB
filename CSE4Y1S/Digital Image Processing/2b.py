
# Take grayscale image of size 512x512 and perform the following operations – 
# Differentiate the results of power law transform and inverse logarithmic transform



import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def power_law_transformation(img,gama):
    row,col=img.shape
    pow_img = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            pow_img[i, j] = img[i, j] ** gama
    return pow_img

def inverse_log_transformation(img,c=1):
    img=img/255
    row,col=img.shape
    inverse_log_img = np.zeros((row, col))
    for i in range(row):
        for j in range(0, col):
            inverse_log_img[i][j] = np.exp(img[i][j]) ** (1 / c) - 1

    return inverse_log_img

def main():
    img = cv2.imread("../images/tiger.jpeg", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # Apply inverse logarithmic transformation
    inverse_log_transformed_img=inverse_log_transformation(img,c=1)
    # Apply power law transformation
    power_transformed_img=power_law_transformation(img,gama=0.3)
    
    # print
    plt.subplot(3, 1, 1)
    plt.imshow(img,cmap='gray')
    plt.title('Original image')
    plt.subplot(3, 1, 2)
    plt.imshow(power_transformed_img,cmap='gray')
    plt.title('Power-law trandformed image')
    
    plt.subplot(3, 1, 3)
    plt.imshow(inverse_log_transformed_img,cmap='gray')
    plt.title('Inverse-log trandformed image')
        
    plt.show()

if __name__ == "__main__":
    main()
