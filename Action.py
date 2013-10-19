import win32api,win32con
import os
from win32api import GetSystemMetrics,GetCursorPos
"""
You need install Python for Windows extension first.
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
@func ScreenSize() ->tuple(width,height)
@func MoveCursor(int x,y)
@func ClickMouse()
@func SystemShutDown()
@func InitSwitchWindows()
@func SwitchWindows() 
@func EndSwitchWindows()
"""

#SCREEN_RESOLUTION
def ScreenSize():
	return (GetSystemMetrics(0),GetSystemMetrics(1))

#MOVE_MOUSE
def MoveCursor(x,y):
	win32api.SetCursorPos((x,y))
	
#CLICK_MOUSE
def ClickMouse():
	x,y = GetCursorPos()
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#SYSTEM_SHUT_DOWN
def SystemShutDown():
	os.system("shutdown -r -t 1")


#DESTROY_WINDOW
def DestroyWindow():
	
	


#SWITCH_WINDOWS
def InitSwitchWindows():
	win32api.keybd_event(0x5B,0,0,0)
	win32api.keybd_event(0x09,0,0,0)
	win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)
	
def SwitchWindowsForward():
	win32api.keybd_event(0x09,0,0,0)
	win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)

def SwitchWindowsBackward():
	win32api.keybd_event(0x09,0,0,0)
	win32api.keybd_event(0x10,0,0,0)
	win32api.keybd_event(0x10,0,win32con.KEYEVENTF_KEYUP,0)
	win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)
	
def EndSwitchWindows():
	win32api.keybd_event(0x5B,0,win32con.KEYEVENTF_KEYUP,0)
	
def SW():
	InitSwitchWindows()
	SwitchWindows()
	EndSwitchWindows()
	