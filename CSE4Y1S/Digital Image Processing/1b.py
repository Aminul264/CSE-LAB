# Take grayscale image of size 512x512 and perform the following operations - 

# Decrease it intensity level resolution by one bit up to reach its binary format observe its change when displaying in the same window size

import cv2
import matplotlib.pyplot as plt
import numpy as np


def ReduceImageByOneBit(img,bit):
    row,col=img.shape
    temp=np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            intensity=img[i][j]/256.0
            intensity=(np.floor(intensity*(2**bit)))
            temp[i][j]=intensity
    
    return temp

def main():
    img=cv2.imread('../images/tiger.jpeg',cv2.IMREAD_GRAYSCALE)
    row,col=512,512
    img=cv2.resize(img,(row,col))
    plt.imshow(img,cmap='gray')
    
    imgList=[]
    # 
    bit=8
    for bit in range(8,0,-1):
        BitReduce_img=ReduceImageByOneBit(img,bit)
        imgList.append(BitReduce_img)
        
    # print
    for i in range(len(imgList)):
        plt.subplot(3,3,i+1)
        plt.imshow(imgList[i],cmap='gray')
        plt.title(f'{8-i}-bit image')
         
    plt.show()
    
if __name__=='__main__':
    main()