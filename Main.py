
#from Capture.py import GetFrame
#import GestureRecognition.py
#import Actions.py

"""
@type point = (int x, int y, int a); 0<=x<=1, 0<=y<=1, 0<=a<=1
@type frame = [int timestamp, point p0, [point p1, [...]]];
@type gesture = (int threshold, func recognize, func action);
@type gestures_list = [gesture g0, [gesture g1, [...]]]; 0 =< threshold, 
@type thresholds_list = [int threshold0, [int threshold1, [...]]]

@global gestures_list Gestures: stores all gestures and their related functions
@global prev_f: the previous frame captured

@import func GetFrame()
    returns the current frame.

@func Recognize_Gestrue(frame f)
    for each gesture in Gestures call recognize(f) with each frame.
@func UpdateCounters(thresholds_list l)
    for each gesture in Gestures apply l to threshold.
    Change negative threshold to 0.
@func CheckCounters()
    for each gesture in Gestures call action() when threshold > 100 
@func GUI()
    handles GUI
"""

#@type frame
prev_f = []

#@type gestures_list
Gestures = []


prev_f = GetFrame()
while True:
    UpdateCounters(Recognize_Gestrue(GetFrame()))
    CheckCounters()
    if GUI()
        return 0
