# 1_A.py



# import cv2
# import matplotlib.pyplot as plt
# import numpy as np


# def main():
#     img=cv2.imread('images/a.jpg',0)
#     height,width=512,512
#     img=cv2.resize(img,(height,width))

#     img_list=[]
#     img_list.append(img)
#     f=2

#     for i in range(0,8):
#         h,w=img.shape
#         img2=np.zeros((h//f,w//f),dtype=np.uint8)
#         for j in range(0,h//f):
#             for k in range(0,w//f):
#                 img2[j][k]=img[j*f][k*f]
        
#         img_list.append(img2)
#         img=img2
    
#     for i in range(0,8):
#         plt.subplot(3,3,i+1)
#         plt.imshow(img_list[i],cmap='gray')


#     # plt.imshow(img,cmap='gray')
#     plt.show()
  



# if __name__=='__main__':
#     main()





# import cv2
# import matplotlib.pyplot as plt
# import numpy as np


# def main():
#     img=cv2.imread('images/a.jpg',0)
#     plt.imshow(img,cmap='gray')
#     plt.show()


# if __name__=='__main__':
#     main()


# 1_B.py

# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# img=cv2.imread('images/brain.jpg',0)
# img=cv2.resize(img,(512,512))



# def function(img,bit):
#     L=2**bit
#     height,width=img.shape
#     outputImg=np.zeros((height,width),dtype=np.uint8)
    
#     for i in range (0,height):
#         for j in range (0,width):
#             temp=img[i][j]/256.0
#             outputImg[i][j]=np.uint8(np.floor(temp*L))
#     print(outputImg)
#     return outputImg






# bit=8
# for i in range (1,9):
#     modified_img=function(img,bit)

#     plt.subplot(3,3,i)
#     plt.imshow(modified_img,cmap='gray')
#     bit-=1

# plt.show()

#  .........1(c).............

# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# img=cv2.imread('images/a.jpg',0)
# img=cv2.resize(img,(512,512))

# hist=np.zeros(256,dtype='uint8')
# height,width=img.shape

# for i in range (0,height):
#     for j in range(0,width):
#         hist[img[i][j]]+=1


# plt.subplot(3,1,1)
# plt.imshow(img,cmap='gray')

# plt.subplot(3,1,2)
# x=np.arange(0,256,1)
# plt.bar(x,hist)


# thresold_img=np.zeros((img.shape),dtype=np.uint8)
# thresold_point=np.mean(img)

# for i in range(0,height):
#     for j in range(0,width):
#         if (img[i][j]>thresold_point):
#             thresold_img[i][j]=255

# hist2=np.zeros(256,dtype=np.uint8)

# for i in range (0,height):
#     for j in range(0,width):
#         hist2[thresold_img[i][j]]+=1

# plt.subplot(3,1,3)
# # plt.imshow(thresold_img,cmap='gray')
# plt.bar(x,hist2)
# plt.show()




# ..................2(a)............
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np

# img=cv2.imread('images/a.jpg',0)
# img=cv2.resize(img,(512,512))


# def function (img):
#     height,width=img.shape
#     img3=img.copy()
#     start_point=int(input('Enter starting point : '))
#     end_point=int(input('Enter ending point : '))
#     add_value=int(input('adding value of intensity : '))

#     for i in range (0,height):
#         for j in range (0,width):
#             if (img[i,j]>=start_point) and (img[i,j]<=end_point):
#                 img3[i,j]+=add_value
#             if img3[i,j]>255:
#                 img3[i][j]=254
#             # else img[i,j]=img[i][j]
    
#     return img3


# plt.subplot(2,1,1)
# plt.imshow(img,cmap='gray')
# plt.title("Orginal image")

# img2=function(img)
# plt.subplot(2,1,2)
# plt.imshow(img2,cmap='gray')
# plt.title("After changing brithness of the image")
# plt.show()



# ................2(b)..............................


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# img=cv2.imread("images/a.jpg",0)
# img=cv2.resize(img,(512,512))


# plt.subplot(2,2,1)
# plt.imshow(img,cmap='gray')
# plt.title('orginal image')



# #power log
# height,width=img.shape
# power_image=np.zeros((img.shape),dtype=np.uint8)

# for i in range (0,height):
#     for j in range (0,width):
#         pixel=(img[i,j]/255.0)**0.5
#         power_image[i,j]=(pixel*255)



# power_image=np.uint8(power_image)
# plt.subplot(2,2,2)
# plt.imshow(power_image,cmap='gray')
# plt.title("power image")



# #invers log
# inver_log=np.zeros((img.shape),dtype=np.uint8)

# for i in range (0,height):
#     for j in range(0,width):
#         pixel=10**((img[i,j]/255.0)-1)
#         inver_log[i,j]=(pixel*255)

# inver_log=np.uint8(inver_log)
# plt.subplot(2,2,3)
# plt.imshow(inver_log,cmap='gray')
# plt.title("inver log image")

# diff_img=cv2.absdiff(power_image,inver_log)
# plt.subplot(2,2,4)
# plt.imshow(diff_img,cmap='gray')
# plt.title('difference image')
# plt.show()




# ............2(c)..................

# import matplotlib.pyplot as plt
# import cv2
# import numpy as np

# img=cv2.imread('images/a.jpg',0)
# img=cv2.resize(img,(512,512))

# mask=0b11100000

# img2=img.copy()

# height,widht=img.shape
# for i in range (0,height):
#     for j in range (0,widht):
#         img2[i,j]=img2[i,j]&mask


# plt.subplot(2,1,1)
# plt.imshow(img,cmap='gray')

# plt.subplot(2,1,2)
# plt.imshow(img2,cmap='gray')
# plt.show()


# .......................3(a)............

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
from math import log10,sqrt


def add_noise(img):
    height,widht=img.shape
    number_of_pixels=random.randint(300,100000)
    for i in range (number_of_pixels):
        x=random.randint(0,height-1)
        y=random.randint(0,widht-1)
        img[x,y]=255

    for i in range (number_of_pixels):
        x=random.randint(0,height-1)
        y=random.randint(0,widht-1)
        img[x,y]=0
    
    return img



def medianF(img):
    med_img=img.copy()
    row,col=img.shape
    n=7
    array=[]
    s=n//2
    for i in range (s,row-s):
        for j in range (s,col-s):
            array=[]
            for k in range (i-s,i+s+1):
                for l in range(j-s,j+s+1):
                    array.append(img[k,l])
            sorted(array)
            med_img[i,j]=array[len(array)//2]
    return med_img

def avg(img):
    row,col=img.shape
    n=7
    outputImg=img.copy()
    s=n//2
    for i in range (s,row-s):
        for j in range (s,col-s):
            temp=0
            for k in range (i-s,i+s+1):
                for l in range (j-s,j+s+1):
                    temp+=img[k,l]
            outputImg[i,j]=temp/(n*n)
    return outputImg


def psnr(img1,img2):
    mes=np.mean((img1-img2)**2)
    if(mes==0):
        return 100
    max_pixel=255.0
    psnrr=20*log10((max_pixel)/sqrt(mes))
    return psnrr

img=cv2.imread('images/a.jpg',0)
img=cv2.resize(img,(512,512))

plt.subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.title('orginal image')

plt.subplot(3,3,2)
img2=add_noise(img)
plt.imshow(img2,cmap='gray')
plt.title('noisy image')



img3=avg(img2)
plt.subplot(3,3,3)
plt.imshow(img3,cmap='gray')
plt.title('avarage filtering')



img4=medianF(img2)
plt.subplot(3,3,4)
plt.imshow(img4,cmap='gray')
plt.title('median filtering img')



plt.show()
