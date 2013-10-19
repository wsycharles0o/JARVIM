import win32api,win32con,win32gui
import os
import time
from operator import abs
from win32api import GetSystemMetrics,GetCursorPos
from win32con import VK_LWIN,VK_TAB,VK_SHIFT
from win32gui import GetForegroundWindow
"""
You need install Python for Windows extension first.
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
@func ScreenSize() ->tuple(width,height)
@func ClickMouse()
@func SystemShutDown()
@func MinimizeWindow()
@func CloseWindow()
@func InitSwitchWindows()
@func SwitchWindowsForward() 
@func SwitchWindowsBackward()
@func EndSwitchWindows()
@func ResizeWindow()
"""

#SCREEN_RESOLUTION
def ScreenSize():
	return (GetSystemMetrics(0),GetSystemMetrics(1))

#MOVE_MOUSE
def MoveCursor(x,y):
        if x is None or y is None: return
        size = ScreenSize()
        new_x = (1-x)*size[0]
        new_y = y*size[1]
        int_x = int(new_x)
        int_y = int(new_y)
        prev_x,prev_y = GetCursorPos()
        if abs(x-prev_x) > 50 or abs(y-prev_y) > 50:
            win32api.SetCursorPos((int_x,int_y))
	
#CLICK_MOUSE
def ClickMouse():
	PressMouse()
        ReleaseMouse()
_released = True
def PressMouse():
    global _released
    if _released: 
        x,y = GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        _released = False
def ReleaseMouse():	
    global _released
    if not _released: 
        x,y = GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        _released = True
#SYSTEM_SHUT_DOWN
def SystemShutDown():
	os.system("shutdown -r -t 1")

#MINIMIZE_WINDOW
def MinimizeWindow():
	win32gui.CloseWindow(GetForegroundWindow())

#CLOSE_WINDOW
def CloseWindow():
	win32gui.SendMessage(win32gui.GetForegroundWindow(),win32con.WM_CLOSE,None,None)

#SWITCH_WINDOWS
def InitSwitchWindows():
	win32api.keybd_event(VK_LWIN,0,0,0)
	win32api.keybd_event(VK_TAB,0,0,0)
	win32api.keybd_event(VK_TAB,0,win32con.KEYEVENTF_KEYUP,0)
	
def SwitchWindowsForward():
	win32api.keybd_event(VK_TAB,0,0,0)
	win32api.keybd_event(VK_TAB,0,win32con.KEYEVENTF_KEYUP,0)

def SwitchWindowsBackward():
	win32api.keybd_event(VK_SHIFT,0,0,0)
	win32api.keybd_event(VK_TAB,0,0,0)
	win32api.keybd_event(VK_TAB,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.keybd_event(VK_SHIFT,0,win32con.KEYEVENTF_KEYUP,0)
	
def EndSwitchWindows():
	win32api.keybd_event(VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0)
	
	
	