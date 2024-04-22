import cv2
import numpy as np

img=cv2.imread('Vp.png',0)
m,n=img.shape
L=img.max()

neg_img=L-img

cv2.imwrite('1Neg_sample.png',neg_img)

flip_img=np.fliplr(img)
#flip_img=np.flipud(img)
cv2.imwrite('1Flipud_sample.png',flip_img)

# Thresholding without background 
# Let threshold =T
# Let pixel value in the original be denoted by r
# Let pixel value in the new image be denoted by s
# If r<T, s= 0
# If r>T, s=255
  
T = L/2
 
# create an array of zeros
img_thresh = np.zeros((m,n), dtype = int) 

  
for i in range(m):
     
    for j in range(n):
         
        if img[i,j] <  T: 
            img_thresh[i,j]= 0
        else:
            img_thresh[i,j] = 255
  
  
# Convert array to png image
cv2.imwrite('2Sample_Thresh.png', img_thresh)

max=img.max()
min=img.min()
for gamma in [0.1, 0.5, 1.2, 2.2]: 
      
    # Apply gamma correction. 
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 
  
    # Save edited images. 
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected) 

