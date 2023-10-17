
# Take grayscale image of size 512x512, add some salt & pepper noise and perform the following operations –
# Apply average and median spatial filters with 5x5 mask and observe their performance for noise suppression in term of PSNR  
# Use different size of mask (3x3, 5x5, 7x7) with average filter for noise suppression and observe their performance in term of PSNR


import cv2
import matplotlib.pyplot as plt
import random
import numpy as np
from math import sqrt ,log10

def add_noise(img):
    temp=np.copy(img)
    row,col=temp.shape
    #amount of noise  in between 400 and 1000
    amount_of_noise=random.randint(8000,10000)
    
    #some random pixel & add salt noise to these pixels
    for i in range(amount_of_noise):
        x_axis=random.randint(0,row-1)
        y_axis=random.randint(0,col-1)
        temp[x_axis][y_axis]=255
    #some random pixel & add peeper noise to these pixels   
    for i in range(amount_of_noise):
        x_axis=random.randint(0,row-1)
        y_axis=random.randint(0,col-1)
        temp[x_axis][y_axis]=0
    return temp

def average_filter(img,mask_size):
    temp=np.copy(img)
    row,col=img.shape
    

    n=mask_size
    # select the area
    left=n//2
    right=left+1 #before end
    sum=0
    for i in range(left,row-left): # from starting  to ending index for row processing
        for j in range(left,col-left): # from starting  to ending index for column
            sum=0
            for k in range(i-left,i+right):
                for l in range(j-left,j+right):
                    sum+=temp[k][l]
            temp[i][j]=sum/(n*n)#mask size
    return temp

def median_filter(img,mask_size):
    temp=np.copy(img)
    row,col=img.shape
    
    # mask size
    n=mask_size
    start=n//2
    end=start+1
    
    for i in range(start,row-end):
        for j in range(start,col-end):
            list=[]
            for k in range(i-start,i+end):
                for l in range(j-start,j+end):
                    list.append(img[k][l])
            sorted(list)
            temp[i][j]=list[len(list)//2]#store middle value
    
    return temp

def PSNR(original, compressed): 
    mse=np.mean((original-compressed)**2)#mse-mean square error
    L=256
    psnr=20*log10((L-1)/mse)
    return psnr

def main():
    img =cv2.imread('../images/rose.jpg',cv2.IMREAD_GRAYSCALE)
    row,col=512,512
    img=cv2.resize(img,(row,col))
    
    #add noise
    noisy_img=add_noise(img)
    # average filter
    avg_filtered_img=average_filter(noisy_img,mask_size=7)
    # Mediun filter
    mediun_filtered_img=median_filter(noisy_img,mask_size=7)
    
    
    
    #print
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original image')
    
    plt.subplot(2,2,2)
    plt.imshow(noisy_img,cmap='gray')
    plt.title('noisy image')
    # average img
    plt.subplot(2,2,3)
    plt.imshow(avg_filtered_img,cmap='gray')
    plt.title('Average filtered image')
    # mediun image
    plt.subplot(2,2,4)
    plt.imshow(mediun_filtered_img,cmap='gray')
    plt.title('Mediun filtered image')
    
    psnr1=PSNR(img,avg_filtered_img)
    psnr2=PSNR(img,mediun_filtered_img)
    
    print(f"PSNR of Average filtered img {psnr1}")
    print(f"PSNR of Median filtered img {psnr2}")
    
    plt.show()
    
if __name__=='__main__':
    main()

