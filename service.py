"""Kodi builtin imports"""
import xbmcgui
import xbmc
import xbmcaddon
import xbmcvfs

"""Needed for paths and stuff"""
from os.path import join
from sys import path

"""Debugging"""
import web_pdb;  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

"""Execute debugging"""
web_pdb.set_trace()  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

"""Required imports, appends controllers to sys.path in order that Kodi can import addon_add_paths.py"""
from resources.lib.controllers import addon_add_paths

"""Required imports"""
from resources.lib.controllers.update_manager import updateManager
from resources.lib.controllers.logger import Logger

"""Create dialog object for displaying informations"""
dialog = xbmcgui.Dialog()

if (updateManager.getIsUpdated()):
    dialog.notification('xPress', 'Erfolgreich aktualisiert', xbmcgui.NOTIFICATION_INFO,
                        2000, True)
    xbmc.sleep(2000)
updateState = updateManager.isUpdate()
if (updateState):
    dialog.notification('xPress', 'Ein neues Update ist verfügbar und wird installiert', xbmcgui.NOTIFICATION_INFO,
                        2000, True)
    updateManager.setIsUpdated(True)
    updateManager.forceRepoUpdate()
elif (updateState) == False:
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 2000, True)
else:
    dialog.notification('xPress', 'Updateprozess wurde abgebrochen, siehe Details: kodi.log',
                        xbmcgui.NOTIFICATION_ERROR, 5000, True)
