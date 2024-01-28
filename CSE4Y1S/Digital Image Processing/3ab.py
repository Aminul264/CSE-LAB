
# Take grayscale image of size 512x512, add some salt & pepper noise and perform the following operations –
# Apply average and median spatial filters with 5x5 mask and observe their performance for noise suppression in term of PSNR  
# Use different size of mask (3x3, 5x5, 7x7) with average filter for noise suppression and observe their performance in term of PSNR


import matplotlib.pyplot as plt
import numpy as np
import cv2

def add_noise(img):
    # amount of noise
    n=np.random.randint(50000,90000)
    row,col=img.shape
    temp=np.copy(img)
    # salt noise in some random pixels
    for i in range(n):
        x=np.random.randint(0,row-1)
        y=np.random.randint(0,col-1)
        temp[x,y]=255
    # peeper noise in some randome pixels
    for i in range(n):
        x=np.random.randint(0,row-1)
        y=np.random.randint(0,col-1)
        temp[x,y]=0
    return temp  

     
def apply_average_filter(noisy_img,mask):
    
    temp=np.copy(noisy_img)
    pad=mask//2
    padded_img=np.pad(noisy_img,((pad,pad),(pad,pad)))#(top,botto),(left,right)
    row,col=padded_img.shape
    
    for r in range(pad,row-pad):
        for c in range(pad,col-pad):
            sum=0
            for i in range(-pad,pad+1):
                for j in range(-pad,pad+1):
                    nr=r+i
                    nc=c+j
                    sum+=padded_img[nr,nc]
            temp[r-pad,c-pad]=sum/(mask**2)
            
    return (temp)

def calculate_psnr(img1,img2):
    
    img1,img2=np.float64(img1),np.float64(img2)
    mse=np.mean((img1-img2)**2)
    if mse==0:
        return float('inf')
    psnr=20*np.log10(255.0)-10*np.log10(mse)
    
    return round(psnr,2)
               
def main():
    img=cv2.imread('../images/MotherBoard.png',0)
    img=cv2.resize(img,(512,512))
    noisy_img=add_noise(img)
    
    plt.subplot(2,2,1)
    plt.imshow(noisy_img,cmap='gray')
    plt.title('noisy image')
    k=1
    for i in range(3,8,2):
        tmp=apply_average_filter(noisy_img,mask=i)
        psnr=calculate_psnr(tmp,img)
        # tmp=cv2.blur(noisy_img,(i,i))
        # psnr = cv2.PSNR(img, tmp)
        k+=1
        plt.subplot(2,2,k)
        plt.imshow(tmp,cmap='gray')
        plt.title(f' avg filter,mask :{i}x{i} psnr:{psnr}')
        
    
    # plt.subplot(2,2,4)
    # plt.imshow(cv2.blur(noisy_img,(5,5)),cmap='gray')
    # plt.title('built-in average filter')
    
    
    
    plt.tight_layout()
    plt.show()
if __name__=='__main__':
    main()
