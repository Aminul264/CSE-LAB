#Take grayscale image of size 512x512, add some salt & pepper noise and perform the following operations –
#3(c)Apply harmonic and geometric mean filter on the noisy image and compare their performance with PSNR

#Geometric Mean:
# [product(f(x,y)]**(1/(mask_size*mask_size))
# Achieves similar smoothing to the arithmetic mean, but tends to lose less image detail

# Harmonic Mean:
# [mask_size*mask_size]/[sum( 1/f(x,y) )]
# Works well for salt noise, but fails for pepper noise

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
    padded_image=np.pad(img,((pad,pad),(pad,pad)),mode='constant')
    row,col=padded_image.shape
    
    for r in range(pad,row-pad):
        for c in range(pad,col-pad):
            neighborhood=0
            for i in range(-pad,pad+1):
                for j in range(-pad,pad+1):
                    nr=r+i
                    nc=c+j
                    if (padded_image[nr][nc]!=0.0):
                        neighborhood+=(1/padded_image[nr][nc])
            if (neighborhood!=0.0):
                 temp[r-pad][c-pad]=(mask_size*mask_size)/neighborhood
    return temp

def geometric_mean_filter(img,mask_size):
    
    temp=np.copy(img)
    pad=mask_size//2
    padded_image=np.pad(img,((pad,pad),(pad,pad)),mode='constant',constant_values=1)
    row,col=padded_image.shape
    
    for r in range(pad,row-pad):
        for c in range(pad,col-pad):
            neighborhood=1
            for i in range(-pad,pad+1):
                for j in range(-pad,pad+1):
                    nr=r+i
                    nc=c+j
                    neighborhood *= (padded_image[nr,nc]+1e-6)
            temp[r-pad, c-pad] = (neighborhood) ** (1 / (mask_size**2))
            
    return temp
    
def calculate_psnr(img1,img2):
    
    img1,img2=np.float64(img1),np.float64(img2)
    mse=np.mean((img1-img2)**2)
    psnr=20*np.log10(255.0)-10*np.log10(mse)    
    return round(psnr,2)

def add_salt_noise(img):
    # number of noise
    temp=np.copy(img)
    h,w=img.shape
    n=np.random.randint(40000,90000)
    for i in range(n):
        x=np.random.randint(0,h)
        y=np.random.randint(0,w)
        temp[x,y]=255
    return temp

def main():
    img=cv2.imread('../images/MotherBoard.png',cv2.IMREAD_GRAYSCALE)
    row,col=512,512
    img=cv2.resize(img,(row,col))
    noisy_img=add_salt_noise(img)
    
    geometric_mean_filtered_img=geometric_mean_filter(noisy_img,mask_size=5)
    harmonic_mean_filtered_img=harmonic_mean_filter(noisy_img,mask_size=5)
    psnr1=calculate_psnr(img,geometric_mean_filtered_img)
    psnr2=calculate_psnr(img,harmonic_mean_filtered_img)
    
    
    
    plt.subplot(2,2,1)
    plt.imshow(noisy_img,cmap='gray')
    plt.title('noisy image')
        
        
    plt.subplot(2,2,2)
    plt.imshow(geometric_mean_filtered_img,cmap='gray')
    plt.title(f'geometric, psnr:{psnr1}')
    
    plt.subplot(2,2,3)
    plt.imshow(harmonic_mean_filtered_img,cmap='gray')
    plt.title(f'harmonic mean, psnr:{psnr2}') 
    
    plt.tight_layout()
    plt.show()
     
if __name__=='__main__':
    main()
