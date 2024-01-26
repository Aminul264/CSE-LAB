# #Take grayscale image of size 512x512 and perform the following operations - 
# # Decrease it's spatial resolution by half every time and observe its change when displaying in the same window size

import cv2
import numpy as np
import matplotlib.pyplot as plt

def decrease_spatial_resolution(img):
    img_list=[]
    img_list.append(img)
    
    while True:
        h,w=img.shape
        if h<1:
            break
        else:
            temp_img=np.zeros((h//2,w//2),np.uint8)
            for i in range(0,h//2):
                for j in range(0,w//2):
                    temp_img[i,j]=img[i*2,j*2]
            img_list.append(temp_img)
            img=temp_img
            
    return img_list
                    
def main():
    img=cv2.imread('../images/rose.jpg',0)
    img = cv2.resize(img, (512, 512))
    
    img_list=decrease_spatial_resolution(img)
    length=len(img_list)

    for i in range(9):
        plt.subplot(3,3,i+1)
        plt.imshow(img_list[i],cmap="gray")
        h,w=img_list[i].shape
        plt.title(f'{h}x{w}')
    plt.tight_layout()    
    plt.show()
    
if __name__=='__main__':
    main()