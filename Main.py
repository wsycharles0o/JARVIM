
#from Capture.py import get_frame
#import GestureRecognition.py
#import Actions.py

"""
@type point = (int x, int y, int a); 0<=x<=1, 0<=y<=1, 0<=a<=1
@type frame = [int timestamp, point p0, [point p1, [...]]];
@type gesture = (int threshold, func recognize, func action);
@type gestures_list = [gesture g0, [gesture g1, [...]]]; 0 =< threshold, 
@type thresholds_list = [int threshold0, [int threshold1, [...]]]

@global gestures_list Gestures: stores all gestures and their related functions
@global frame Prev_f: the previous frame captured

@import func get_frame()
    returns the current frame.

@func recognize_gestrue(frame f)
    for each gesture in Gestures call recognize(f) with each frame.
@func update_counters(thresholds_list l)
    for each gesture in Gestures apply l to threshold.
    change negative threshold to 0.
@func check_counters()
    for each gesture in Gestures call action() when threshold > 100 
@func GUI()
    handles GUI
@func initialization()
    build Gestures.
"""

#@type frame
Prev_f = []

#@type gestures_list
Gestures = []


def recognize_gestrue(frame):
    global Gestures, Prev_f
    l = []
    for g in Gestures:
        l.append(g[1](Prev_f, frame))
    prev_f = frame
    return l

def update_counters(l):
    global Gestures
    for i in len(Gestures):
        Gestures[i][0] += l[i]
        if Gestures[i][0] < 0:
            Gestures[i][0] = 0

def check_counters():
    global Gestures
    for g in Gestures:
        if g[0] >= 100:
            g[2]()
            g[0] = 0

def GUI():
    pass

def initialization():
    pass

initialization()
Prev_f = get_frame()
while True:
    update_counters(recognize_gestrue(get_frame()))
    check_counters()
    if GUI()
        return 0
