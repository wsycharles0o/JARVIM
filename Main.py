import sys
import time
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
@global timestamp Pre_act

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

#@type timestamp
Pre_act = time.time()

def recognize_gestrue(frame):
    print "R({0})\nG({1})\nB({2})\n\n".format(frame[1],frame[2],frame[3])
    global Gestures, Prev_f
    l = []
    for g in Gestures:
        l.append(g[1](Prev_f, frame))
    Prev_f = frame
    return l

def update_counters(l):
    global Gestures
    #print "{0} {1}".format(l[0], l[1]) #TEST CODE
    for i in range(len(Gestures)):
        Gestures[i][0] += l[i]
        if Gestures[i][0] < 0:
            Gestures[i][0] = 0

def check_counters():
    global Gestures, Pre_act
    for g in Gestures:
        if g[0] >= 100 and (time.time() - Pre_act) > 2.0 :
            g[2]()
            g[0] = 0
            Pre_act = time.time()


"""UNFINISHED: REMEMBER TO CHANGE THIS!!!"""
def GUI():
    return False

def initialization():
    CP.init(True, ["Red", "Green", "Blue"])
    if not CP.camara_available(): sys.exit("WHERE IS YOUR CAMERA!?!?")
    Gestures.append([0,GR.swipe_left_recognize,t1])
    Gestures.append([0,GR.swipe_right_recognize,t2])

def get_frame():
    return CP.get_frame(
    [
    ((160,145,60),(180,256,256)),
    ((19,40,60),(35,256,256)),
    ((65,20,60),(105,256,256)),
    ]
    )


initialization()
Prev_f = get_frame()
while True:
    update_counters(recognize_gestrue(get_frame()))
    check_counters()
    if GUI():
        sys.exit(0)

