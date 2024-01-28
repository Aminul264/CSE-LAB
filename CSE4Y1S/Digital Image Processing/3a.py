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
def apply_median_filter(noisy_img,mask):
    
    temp=np.copy(noisy_img)
    pad=mask//2
    padded_img=np.pad(noisy_img,((pad,pad),(pad,pad)))
    row,col=padded_img.shape
    
    for r in range(pad,row-pad):
        for c in range(pad,col-pad):
            neighbour=[]
            for i in range(-pad,pad+1):
                for j in range(-pad,pad+1):
                    nr=r+i
                    nc=c+j
                    x=padded_img[nr,nc]
                    neighbour.append(x)
            neighbour=sorted(neighbour)
            temp[r-pad,c-pad]=neighbour[len(neighbour)//2]
    
    return temp
     
def apply_average_filter(noisy_img,mask):
    
    temp=np.copy(noisy_img)
    pad=mask//2
    padded_img=np.pad(noisy_img,((pad,pad),(pad,pad)))#(top,botto),(left,right)
    row,col=padded_img.shape
    print(row,col)
    
    for r in range(pad,row-pad):
        for c in range(pad,col-pad):
            sum=0
            for i in range(-pad,pad+1):
                for j in range(-pad,pad+1):
                    nr=r+i
                    nc=c+j
                    sum+=padded_img[nr,nc]
            temp[r-pad,c-pad]=sum/(mask**2)
            
    return np.uint8(temp)

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
    avgf_img=apply_average_filter(noisy_img,mask=5)
    medianf_img=apply_median_filter(noisy_img,mask=5)
    psnr1=calculate_psnr(img,avgf_img)
    psnr2=calculate_psnr(img,medianf_img)
    psnr=calculate_psnr(img,noisy_img)
    
    # display plot
    plt.subplot(2,2,1)
    plt.imshow(noisy_img,cmap='gray')
    plt.title(f'noisy image ,psnr :{psnr}')
    plt.subplot(2,2,2)
    plt.imshow(avgf_img,cmap='gray')
    plt.title(f'average filter image ,psnr: {psnr1}')
    plt.subplot(2,2,3)
    plt.imshow(medianf_img,cmap='gray')
    plt.title(f'median filtered img, psnr2 : {psnr2}')
    
    # plt.subplot(2,2,4)
    # plt.imshow(cv2.medianBlur(noisy_img,(5)),cmap='gray')
    # plt.title('built-in  median filter')
    
    # plt.subplot(2,2,4)
    # plt.imshow(cv2.blur(noisy_img,(5,5)),cmap='gray')
    # plt.title('built-in average filter')
    
    
    
    plt.tight_layout()
    plt.show()
if __name__=='__main__':
    main()