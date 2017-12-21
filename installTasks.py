##
## Switching Keyboard Layout for NVDA
## Copyright (c) 2015 by Code Factory, S.L. All rights reserved.
##

import gui
import wx
import _winreg

## Translators: message box when user is installing the addon in NVDA. 
msg = _("""Thank you for choosing Keyboard Layout Switching add-on. 

This add-on requires to pin the language bar to the task bar in case it is not. 
For this the add-on requires to make some registry changes to your system. 
Also you need to log off and then log on to your system after the add on installation for the changes to reflect.
Would you like to continue ?
""")
ROOT_KEY = r"Software\Microsoft\CTF\LangBar"
langBarPos = 4       #4 specifies language bar pinned to task bar
visibleSettings = 1  #1 specifies that extra icons are visible in the taskbar along with the language bar

def onInstall():
    ## Translators: title of message box when user is installing add-on
    gui.messageBox(msg,"Pin Language bar to task bar", wx.OK)
    k = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, ROOT_KEY, 0, _winreg.KEY_WRITE | _winreg.KEY_WOW64_64KEY)
    _winreg.SetValueEx(k, "ShowStatus", None, _winreg.REG_DWORD,langBarPos)
    _winreg.SetValueEx(k, "ExtraIconsOnMinimized", None, _winreg.REG_DWORD,visibleSettings)