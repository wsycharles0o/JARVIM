import sys
import Capture as CP
import Gesture_Recognition as GR
#import Actions as A

"""
@type point = (int x, int y, int a); 0<=x<=1, 0<=y<=1, 0<=a<=1
@type frame = [int timestamp, point p0, [point p1, [...]]]; point is None if p.a is too small
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

"""
Test Codes Hereforth! 
REMEMBER TO DELETE!!!!
"""

def t1 ():
    print "Left!"

def t2 ():
    print "Right!"
"""
Test Codes Ends.
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
    for i in range(len(Gestures)):
        Gestures[i][0] += l[i]
        if Gestures[i][0] < 0:
            Gestures[i][0] = 0
    #TEST CODE!!!!!!! REMEMBER TO DELETE
    print "l:{0} r:{0}".format(Gestures[0][0], Gestures[1][0])

def check_counters():
    global Gestures
    for g in Gestures:
        if g[0] >= 100:
            g[2]()
            g[0] = 0

"""UNFINISHED: REMEMBER TO CHANGE THIS!!!"""
def GUI():
    return False

def initialization():
    CP.init(False, ["Red","Yellow","Green","Blue"])
    if not CP.camara_available(): sys.exit("WHERE IS YOUR CAMERA!?!?")
    Gestures.append([0,GR.swipe_left_recognize,t1])
    Gestures.append([0,GR.swipe_right_recognize,t2])

def get_frame():
    return CP.get_frame(
    [
    ((160,160,60),(180,256,256)),
    ((17,160,60),(38,256,256)),
    ((38,160,60),(75,256,256)),
    ((90,160,60),(120,256,256)),
    ]
    )


initialization()
Prev_f = get_frame()
while True:
    update_counters(recognize_gestrue(get_frame()))
    check_counters()
    if GUI():
        sys.exit(0)

