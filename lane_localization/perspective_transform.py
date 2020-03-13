import cv2 as cv
import numpy as np

###########################################################

FILE_NAME = "lane_lines.jpg"
PTS = [
    (325, 110),
    (445, 110),
    (715, 340),
    (10, 340)
]
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (100, 175, 100)
]

FONT = cv.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1
LINE_TYPE = cv.LINE_AA

WINDOW_NAME = 'transform'

###########################################################

def mouse_cb (event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)

###########################################################

def draw_pts(pts, colors, img):
    if len(pts) != 4 or len(colors) != 4:
        raise ValueError("Ya done goofed")
    
    cv.line(img, pts[0], pts[3], (180, 230, 85), thickness=3, lineType=LINE_TYPE)
    cv.line(img, pts[1], pts[2], (180, 230, 85), thickness=3, lineType=LINE_TYPE)

    for i, pt in enumerate(pts):
        cv.circle(img, pt, 5, colors[i], thickness=-1)
        origin = (  
            pt[0] - 10,
            pt[1] - 10
        )
        cv.putText(img, str(i + 1), origin, FONT, FONT_SCALE, colors[i], lineType=LINE_TYPE)

###########################################################

def perspective_transform(img, pts):
    rect = np.array(pts, dtype= "float32")
    (tl, tr, br, bl) = pts

    widthA= np.sqrt(
        (tr[0] - tl[0]) ** 2 +
        (tr[1] - tl[1]) ** 2
    )

    widthB= np.sqrt(
        (br[0] - bl[0]) ** 2 +
        (br[1] - bl[1]) ** 2
    )

    maxWidth = max(int(widthA), int(widthB))
    print(maxWidth)

    heightA = np.sqrt(
        (tr[1]- br[1]) ** 2 +
        (tr[0]- br[0]) ** 2
    )

    heightB = np.sqrt(
        (tl[1]- bl[1]) ** 2 +
        (tl[0] - bl[0]) ** 2
    )

    maxHeight = max (int(heightA), int(heightB))
    print(maxHeight)

    dst = np.array([
        [0 , 0],
        [maxWidth-1 , 0],
        [maxWidth-1, maxHeight-1],
        [0 , maxHeight-1]
    ], dtype = "float32")

    #M is a matrix
    M = cv.getPerspectiveTransform(rect, dst)
    return cv.warpPerspective(img, M, (maxWidth, maxHeight))

###########################################################

img = cv.imread(FILE_NAME)
final = img.copy()
cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, mouse_cb)

draw_pts(PTS, COLORS, img)

cv.imshow(WINDOW_NAME, img)
cv.imshow("result", perspective_transform(final, PTS))
cv.waitKey(0)
cv.destroyAllWindows()
