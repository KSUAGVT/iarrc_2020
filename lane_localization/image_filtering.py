import cv2 as cv
import numpy as np

##################################################

IMAGE_PATH = 'straight_road.jpg'
IMAGE_SCALE = 0.2

##################################################

# Read in the image
image = cv.imread(IMAGE_PATH)

# Resize the image by IMAGE_SCALE
width = int(image.shape[1] * IMAGE_SCALE)
height = int(image.shape[0] * IMAGE_SCALE)
image = cv.resize(image, (width, height))

# Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Basic Operations
ret, thresh_binary = cv.threshold(gray, 100, 178, cv.THRESH_BINARY)
ret, thresh_tozero = cv.threshold(gray, 100, 178, cv.THRESH_TOZERO)

# Adaptive Thresholding
blurred = cv.medianBlur(gray, 5)

thresh_adaptive = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 9, 5)
result = cv.bitwise_and(image, image, mask=thresh_adaptive)

# Display the result
cv.imshow("To Zero", thresh_tozero)
cv.imshow("Result", result)
cv.imshow("Adaptive Threshold", thresh_adaptive)
cv.waitKey(0)
cv.destroyAllWindows()
