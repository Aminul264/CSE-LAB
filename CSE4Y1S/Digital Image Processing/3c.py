#Take grayscale image of size 512x512, add some salt & pepper noise and perform the following operations –
#3(c)Apply harmonic and geometric mean filter on the noisy image and compare their performance with PSNR

#Geometric Mean:
# [product(f(x,y)]**(1/(mask_size*mask_size))
# Achieves similar smoothing to the arithmetic mean, but tends to lose less image detail

# Harmonic Mean:
# [mask_size*mask_size]/[sum( 1/f(x,y) )]
# Works well for salt noise, but fails for pepper noise

import cv2
import numpy as np
import matplotlib.pyplot as plt

def harmonic_mean_filter(img,mask_size):
    temp=np.copy(img)
    
    pad=mask_size//2
    row,col=img.shape
    
    for i in range(pad,row-pad):
        for j in range(pad,col-pad):
            neighborhood=0
            for k in range(i-pad,i+pad+1):
                for l in range(j-pad,j+pad+1):
                    if (img[k][l]!=0.0):
                        neighborhood+=(1/img[k][l])
            if (neighborhood!=0.0):
                 temp[i][j]=(mask_size*mask_size)/neighborhood
            # # or
            # neighborhood = img[i-pad:i+pad+1, j-pad:j+pad+1]
            # temp[i, j] = mask_size**2 / np.sum(1 / (neighborhood + 1e-6))
    return temp

def geometric_mean_filter(img,mask_size):
    temp=np.copy(img)
    row,col=img.shape
    pad=mask_size//2
    
    # img=img/255
    for i in range(pad,row-pad):
        for j in range(pad,col-pad):
            neighborhood=1
            for k in range(i-pad,i+pad+1):
                for l in range(j-pad,j+pad+1):
                    neighborhood *= (img[k,l]+1e-6)
            temp[i, j] = (neighborhood) ** (1 / (mask_size**2))
            # or
            # neighborhood = img[i-pad:i+pad+1, j-pad:j+pad+1]
            # temp[i, j] = np.prod(neighborhood+1e-6) ** (1 / (mask_size**2))# 1e-6 means =10**-6=0.000001
    return temp#.astype(np.uint8)
    
def main():
    img=cv2.imread('../images/noisysalterpepper.png',cv2.IMREAD_GRAYSCALE)
    row,col=300,300
    img=cv2.resize(img,(row,col))
    
    mask_size=3
    harmonic_mean_filtered_img=harmonic_mean_filter(img,mask_size)
    geometric_mean_filtered_img=geometric_mean_filter(img,mask_size)
    
    
    
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original')
        
    plt.subplot(2,2,2)
    plt.imshow(harmonic_mean_filtered_img,cmap='gray')
    plt.title('harmonic mean') 
        
    plt.subplot(2,2,3)
    plt.imshow(geometric_mean_filtered_img,cmap='gray')
    plt.title('geometric')
    
    plt.tight_layout()
    plt.show()
     
if __name__=='__main__':
    main()