import api
import globalPluginHandler
from logHandler import log
import addonHandler
import config
import eventHandler
from NVDAObjects.IAccessible import MenuItem
import _winreg

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_accessLanguageBar(self, gesture):
		obj=api.getDesktopObject()
		simpleReviewMode=config.conf["reviewCursor"]["simpleReviewMode"]
		refObject=obj.simpleFirstChild if simpleReviewMode else obj.firstChild
  		while refObject:
  			refObject=refObject.simpleNext if simpleReviewMode else refObject.next
  			if refObject.name == "Language bar":
  				break
  		countOne=refObject.childCount
  		for i in range(0,countOne):
  			if refObject.getChild(i).name== "Settings":
  				break
  		if refObject:
  			refObject.getChild(i).doAction()
  			eventHandler.executeEvent('gainFocus',refObject.getChild(i).next)

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if obj.windowClassName == "CiceroUIWndFrame":
 			clsList.insert(0, LanguageBarMenuItems)
    
	__gestures = {
		"kb:nvda+k" : "accessLanguageBar",
	}
   
class LanguageBarMenuItems(MenuItem):
 	shouldAllowIAccessibleFocusEvent=True