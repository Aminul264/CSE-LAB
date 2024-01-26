# # Take grayscale image of size 512x512 and perform the following operations - 

# # Decrease it intensity level resolution by one bit up to reach its binary format observe its change when displaying in the same window size
import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_img_by_one_bit(img):
    img_list=[]
    h,w=img.shape
    bit=8
    
    for i in range(bit,0,-1):
        temp_img=np.zeros((h,w))
        for j in range(h):
            for k in range(w):
                intensity=img[j,k]/256.0
                temp_img[j,k]=np.floor(intensity*(2**i))
        img_list.append(temp_img)
    
    return img_list

def display(img_list):
    for i in range(len(img_list)):
        plt.subplot(3,3,i+1)
        plt.imshow(img_list[i],cmap='gray')
        plt.title(f'{8-i} bit')
        
    plt.tight_layout()
    plt.show()  
                     
def main():
    img=cv2.imread('../images/brain.jpg',0)
    img=cv2.resize(img,(512,512))
    img_list=reduce_img_by_one_bit(img)
    display(img_list)
    
if __name__=='__main__':
    main()