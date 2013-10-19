__author__="Jacky"
__date__ ="$Oct 18, 2013 6:44:33 PM$"

from cv2 import cv
import cv2
import numpy
from time import time

"""
Sample code for using this frame:
init(True, ["Blue", "Red"]);
if not camara_available(): print "Camera init fail"; return
while(True):
    l = get_frame( [ ((90,160,60),(120,256,256)), ((160,160,60),(180,256,256)) ] )
    if l[1][1]!=None or l[2][1]!=None:
        print "{0}".format(l)
"""

AREA_THRESHOLD = 0.0046 # smaller than this: regard as 0.
capture = None
_debug = False
_color_names = []
CAMERA_WINDOW = "Camera"

def get_image(capture):
    """
    Return (image, time)
    Start grabbing a slide from camera. If can't grab a slide, image is None.
    time: time of capturing.
    """
    image = cv.QueryFrame(capture);
    #image = blur_image(image) # TURN OFF BLURRING HERE
    t = time()
    return (image,t)

def blur_image(image):
    """
    If the image is not None, blur the image. Then return itself.
    """
    if image is not None:
        cv.Smooth(image, image, cv.CV_GAUSSIAN, 3, 3)
    return image

def get_thresholded_image(image, range1, range2):
    """
    range1, range2: init by cv.Scalar(h, s, v)
    """
    img_hsv = cv.CreateImage(cv.GetSize(image), 8, 3);
    cv.CvtColor(image, img_hsv, cv.CV_BGR2HSV);
    img_threshed = cv.CreateImage(cv.GetSize(image), 8, 1);
    cv.InRangeS(img_hsv, range1, range2, img_threshed);
    return img_threshed

def get_point(image, range1, range2, color_num):
    """
    image: a slide from the original video    
    Return a three number tuple: (x, y, area)
        (0~1, 0~1, 0~1), or (None, None, None)
    """
    img_threshed = get_thresholded_image(image, range1,range2)
    w, h = cv.GetSize(image)
    if _debug: cv.ShowImage(_color_names[color_num], img_threshed)
    mat = numpy.asarray(img_threshed[:,:])
    moments = cv2.moments(mat,0)
    moment10 = moments['m10']
    moment01 = moments['m01']
    area = moments['m00']
    small_area =  area / (w * h * 255) # 0~1 scale
    if small_area > AREA_THRESHOLD:
        x = moment10 / area / w # 0~1 scale
        y = moment01 / area / h # 0~1 scale
        area = small_area
    else:
        x = None
        y = None
        area = None
    return (x, y, area)

#Available outside

def init(debug = False, color_names = []):
    """
    Initialization.
    debug: if True, windows would be opened for each color channel.
    color_names: names for each color channel, used for window titles
    Should check predicate camara_available() after initialization.
    """
    global capture
    global _debug
    global _color_names
    capture = cv.CaptureFromCAM(1);
    _debug = debug
    _color_names = color_names
    if _debug:
        cv.NamedWindow(CAMERA_WINDOW)
        for color in _color_names:
            cv.NamedWindow(color)

def camara_available():
    """
    After init(), this predicate should be checked; if false, program should exit.
    """
    return capture is not None

def get_frame(ranges):
    """
    ranges: a list of three elements of (h, s, v)
    Return a list:
    the first element is the time stamp when image is captured
    the rest are three number tuples: (x, y, area)
    Color is considered "found" if area is calculated to be greater than AREA_THRESHOLD
    x: None if color is not found, else color's mid point's x in a 0~1 float scale
    y: None if color is not found, else color's mid point's y in a 0~1 float scale
    area: None if color is not found, else color's area in a 0~1 float scale
    """
    new_ranges = []
    for r in ranges:
        r0 = cv.Scalar(r[0][0], r[0][1], r[0][2])
        r1 = cv.Scalar(r[1][0], r[1][1], r[1][2])
        new_ranges.append((r0,r1))
    if capture:
        image, timestamp = get_image(capture)
        if _debug: cv.ShowImage(CAMERA_WINDOW, image)
        result = [timestamp]
        i = 0
        for (range1, range2) in ranges:
            result.append(get_point(image, range1, range2, i))
            i += 1
        if _debug: cv.WaitKey(10);
        return result
    return [time()] + [None] * len(ranges) # if camera is not found
