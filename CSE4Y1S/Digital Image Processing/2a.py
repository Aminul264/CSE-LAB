# Take grayscale image of size 512x512 and perform the following operations –
 
# Perform the brightness enhancement of a specific range of gray levels and observe its result



import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance(img,range_start,range_end,enhanced_value):
    row,col=img.shape
    tmp_img = np.zeros((row, col))
    for i in range(0, row):
        for j in range(0, col):
            if img[i, j] >= range_start and img[i, j] <= range_end:
                intensity_value = img[i, j] + enhanced_value
                if intensity_value >= 255:
                    intensity_value = 255
                tmp_img[i, j] = intensity_value
            else:
                tmp_img[i, j] = img[i, j]
    return tmp_img

def main():
    img = cv2.imread("../images/tiger.jpeg", cv2.IMREAD_GRAYSCALE)
    row,col=512,512
    img=cv2.resize(img,(row,col))


    enhanced_img=enhance(img,range_start = 100,range_end = 200,enhanced_value = 50)
    # print
    plt.subplot(2,1,1)
    plt.imshow(img,cmap='gray')
    plt.title('Original Image')

    plt.subplot(2,1,2)
    plt.imshow(enhanced_img,cmap='gray')
    plt.title('Enhanced Image')
    
    plt.show()

if __name__ == "__main__":
    main()
