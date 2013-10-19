import win32api,win32con
from win32api import GetSystemMetrics,GetCursorPos
"""
You need install Python for Windows extension first.
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
@func ScreenSize() ->tuple(width,height)
@func MoveCursor(int x,y)
@func ClickMouse()
@func SystemShutDown()
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
	win32api.ExitWindowsEx(4)

#KILL_WINDOWS
def KillWindows
#

#SWITCH_WINDOWS

	
