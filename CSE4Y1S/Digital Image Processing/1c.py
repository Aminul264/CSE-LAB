# Take grayscale image of size 512x512 and perform the following operations - 
# Illustrate the histogram of the image and make single threshold segmentation observed from the histogram

import cv2
import matplotlib.pyplot as plt
import numpy as np

def thresholding(img,threshold):
    h,w=img.shape
    temp_img=np.zeros((h,w),np.uint8)
    for i in range(h):
        for j in range(w):
            if img[i,j]<threshold:
                temp_img[i,j]=0
            else:
                temp_img[i,j]=255
    return temp_img

def histogram(img):
    # hist=[0]*256
    hist=np.zeros(256,np.uint32)
    h,w=img.shape
    for i in range(h):
        for j in range(w):
            hist[img[i,j]]+=1
    return hist
  
def main():
    img=cv2.imread('../images/skleton.png',0)
    img=cv2.resize(img,(512,512))
    threshold=np.mean(img)
    threshold_img=thresholding(img,threshold)
    
    plt.subplot(2,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('original image')
    
    plt.subplot(2,2,2)
    plt.imshow(threshold_img,cmap='gray')
    plt.title('thresold image')
    
    # 
    hist1=histogram(img)
    hist2=histogram(threshold_img)

    
    plt.subplot(2,2,3)
    plt.bar(range(256),hist1)
    plt.title('histogram before thresolding')
    
    plt.subplot(2,2,4)
    plt.bar(range(256),hist2)
    plt.title('histogram after thresolding')
    
    
    plt.tight_layout()
    plt.show()
    
if __name__=='__main__':
    main()
 