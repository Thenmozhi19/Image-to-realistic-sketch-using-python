# -*- coding: utf-8 -*-
"""

@author: thenmozhi19
"""
import cv2
def tosketch(photo, kernal_size):
    #Read Image
    img=cv2.imread(photo)
    
    # Convert to Gray Image
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(gray_img)

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (kernal_size,kernal_size),0)
    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    # Sketch Image
    sketch_img=cv2.divide(gray_img,invblur_img, scale=250.0)

    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_img)
    # Display sketch
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#call sketch function
tosketch(photo='./img.jpg', kernal_size=79)