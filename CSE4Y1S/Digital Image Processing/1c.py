# Take grayscale image of size 512x512 and perform the following operations - 

# Illustrate the histogram of the image and make single threshold segmentation observed from the histogram

import cv2
import matplotlib.pyplot as plt
import numpy as np

def Histogram(img):
    row,col=img.shape
    hist=np.zeros(256,dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            hist[img[i][j]]+=1
    return hist

def Thresolding(img,thresold):
    row,col=img.shape
    temp=np.zeros((row,col),dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            if img[i][j]<thresold:
                temp[i][j]=0
            else:
                temp[i][j]=255
    return temp
    
def main():
    img=cv2.imread('../images/fingerprint.jpg',cv2.IMREAD_GRAYSCALE)
    row,col=512,512
    img=cv2.resize(img,(row,col))
    histo1=Histogram(img)
    
    # thresolding
    thresold=np.mean(img)#take a mean value: thresold point
    thresold_img=Thresolding(img,thresold)
    
    # call histogram
    histo2=Histogram(thresold_img)
    
    
    # print
    plt.subplot(2,2,1)

    plt.imshow(img,cmap='gray')
    plt.title('original image')
    
    plt.subplot(2,2,2)
    plt.bar(range(256),histo1)
    plt.title("histogram-before thresolding")
    
    plt.subplot(2,2,3)
    plt.imshow(thresold_img,cmap='gray')
    plt.title('thresold image')
    
    plt.subplot(2,2,4)
    plt.bar(range(256),histo2)
    plt.title("histogram-after thresolding")
    
    plt.show()

if __name__=='__main__':
    main()