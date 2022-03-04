import xbmcgui
import xbmc
import xbmcaddon
import xbmcvfs

from os.path import join
from sys import path

ADDON_NAME = "plugin.video.xpress"
#import pydevd
#pydevd.settrace('localhost', port=1234, stdoutToServer=True, stderrToServer=True)
#import web_pdb;#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
#web_pdb.set_trace()#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

#addonXpress = xbmcaddon.Addon(ADDON_NAME)
#xpressAddonPath = xbmcvfs.translatePath(addonXpress.getAddonInfo('path'))
#path.append(xpressAddonPath)
#path.append(join(xpressAddonPath, "resources", "lib", "controllers"))


addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
path.append(join(addonPath, "resources", "lib", "controllers"))
from resources.lib.controllers.add_paths import addPaths

from resources.lib.controllers.update_manager import updateManager
from resources.lib.controllers.logger import Logger

"""
    Stopping addon just for safty to not conflict with potential updates
"""
xbmc.executebuiltin("StopScript(addon)")

"""Create dialog object for displaying informations"""
dialog = xbmcgui.Dialog()

updateState = updateManager.isUpdate()
if (updateState is None):
    dialog.notification('xPress', 'Updateprozess wurde abgebrochen, siehe Details: kodi.log', xbmcgui.NOTIFICATION_INFO, 5000, True)
elif (updateState):
    dialog.notification('xPress', 'Ein neues Update ist verfügbar und wird installiert', xbmcgui.NOTIFICATION_INFO, 5000, True)
    xbmc.executebuiltin("UpdateAddonRepos")#After this line code breaks when debug mode is on with pdb web
    xbmc.executebuiltin("UpdateLocalAddons")
    xbmc.executebuiltin("StopScript(addon)")
    #xbmc.sleep(2000)
    ##
else:
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 5000, True)
#Logger.info("Test")

