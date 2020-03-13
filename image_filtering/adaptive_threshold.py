import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

img = cv.imread('lane_lines.jpg', 0)
print(img.shape)

ROWS = 4
COLS = 4

plt.title("Basic Thresholding")

for i in range(ROWS * COLS):
    # assign to the current bucket
    plt.subplot(ROWS, COLS, i + 1)
    
    # get the bounds
    lower = int(255 / 16 * i)
    upper = int(255 / 16 * (i + 1))

    # print the title
    plt.title('[{:}, {:}]'.format(lower, upper))
    
    # get lower thresh 
    thresh_binary = cv.inRange(img, lower, upper)
    
    plt.imshow(thresh_binary, cmap='gray')
    plt.axis('off')



plt.show()

