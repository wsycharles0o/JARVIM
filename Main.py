import sys
import time
import Capture as CP
import Gesture_Recognition as GR
import Action as A

"""
@type point = (int x, int y, int a); 0<=x<=1, 0<=y<=1, 0<=a<=1
@type frame = [int timestamp, point p0, [point p1, [...]]]; point is None if p.a is too small
@type gesture = (int threshold, func recognize, func action);
@type gestures_list = [gesture g0, [gesture g1, [...]]]; 0 =< threshold, 
@type thresholds_list = [int threshold0, [int threshold1, [...]]]

@global gestures_list Gestures: stores all gestures and their related functions
@global frame Prev_f: the previous frame captured
@global timestamp Pre_act
@global timestamp Pre_wintab
@global int WINTAB_TIMEOUT
@global bool wintab_init

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

#@type timestamp
Pre_act = time.time()

#@type timestamp
Pre_wintab = time.time()

#@int
WINTAB_TIMEOUT = 4

#@bool
Wintab_init = False

def recognize_gestrue(frame):
    #TEST CODE
    #print "R({0})\nG({1})\nB({2})\n\n".format(frame[1],frame[2],frame[3])
    global Gestures, Prev_f
    l = []
    for g in Gestures:
        l.append(g[1](Prev_f, frame))
    Prev_f = frame
    return l

def update_counters(l):
    global Gestures
    if not l[0] is l[1]:
        print "{0} {1}".format(l[0], l[1]) #TEST CODE
    for i in range(len(Gestures)):
        Gestures[i][0] += l[i]
        if Gestures[i][0] < 0:
            Gestures[i][0] = 0

def check_counters():
    global Gestures, Pre_act
    for g in Gestures:
        if g[0] >= 100 and (time.time() - Pre_act) > 1.0 :
            g[2]()
            g[0] = 0
            Pre_act = time.time()

def wintab_l():
    global Wintab_init, Pre_wintab
    if not Wintab_init:
        A.InitSwitchWindows()
        Wintab_init = True
    A.SwitchWindowsBackward()
    Pre_wintab = time.time()

def wintab_r():
    global Wintab_init, Pre_wintab
    if not Wintab_init:
        A.InitSwitchWindows()
        Wintab_init = True
    A.SwitchWindowsForward()
    Pre_wintab = time.time()

"""UNFINISHED: REMEMBER TO CHANGE THIS!!!"""
def GUI():
#----------------This Part checks win+tab status----------------
    global Wintab_init, Pre_wintab
    if  Wintab_init and time.time() - Pre_wintab >= WINTAB_TIMEOUT:
        A.EndSwitchWindows()
        Wintab_init = False
#---------------------------------------------------------------


    return False

def initialization():
    CP.init(
    [
    #((150,170,60),(170,256,180)),
    #((19,100,60),(35,256,230)),
    #((65,90,60),(105,256,180)),
    ((160,145,60),(180,256,256)),
    ((12,120,60),(30,200,256)),
    ((65,180,130),(105,256,200)),
    ]
    ,True, ["Red", "Green", "Blue"])
    if not CP.camara_available(): sys.exit("WHERE IS YOUR CAMERA!?!?")
    Gestures.append([0,GR.swipe_left_recognize,t1])
    Gestures.append([0,GR.swipe_right_recognize,t2])
    Gestures.append([0,GR.expand_recognize,t3])
    Gestures.append([0,GR.shrink_recognize,t4])

def get_frame():
    return CP.get_frame()

"""
Test Codes Hereforth! 
REMEMBER TO DELETE!!!!
"""

def t1 ():
    wintab_l()
    print "Left!"

def t2 ():
    wintab_r()
    print "Right!"

def t3 ():
    print "expand"
def t4 ():
    print "shrink"
"""
Test Codes Ends.
"""

initialization()
Prev_f = get_frame()
while True:
    update_counters(recognize_gestrue(get_frame()))
    check_counters()
    if GUI():
        sys.exit(0)

