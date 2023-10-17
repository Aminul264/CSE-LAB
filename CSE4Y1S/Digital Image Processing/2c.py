# Take grayscale image of size 512x512 and perform the following operations – 
# Find the difference image between original and the image obtained by last three bits (MSB)


import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Load the image
    img = cv2.imread('../images/tiger.jpeg', cv2.IMREAD_GRAYSCALE)
    row ,col = 512,512
    img = cv2.resize(img, (row, col))

    # Define the mask
    # mask = 224  # last 3-bit  11100000
    mask = 0b11100000

    modified_img = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            modified_img[i][j] = img[i][j] & mask

    # Find the difference
    diff_img = img - modified_img

    # Plot the images using matplotlib
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original image')

    plt.subplot(2, 2, 2)
    plt.imshow(modified_img, cmap='gray')
    plt.title('most 3 bit Image')

    plt.subplot(2, 2, 3)
    plt.imshow(diff_img, cmap='gray')
    plt.title('Difference Image')

    plt.show()

if __name__ == "__main__":
    main()
