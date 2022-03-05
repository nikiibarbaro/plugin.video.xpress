import xbmcgui
import xbmc
import xbmcaddon
import xbmcvfs

from os.path import join
from sys import path

ADDON_NAME = "plugin.video.xpress"

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
if(updateState):
    dialog.notification('xPress', 'Ein neues Update ist verfügbar und wird installiert', xbmcgui.NOTIFICATION_INFO, 5000, True)
    xbmc.executebuiltin("StopScript({0})".format(ADDON_NAME))
    #xbmc.executebuiltin("UpdateAddonRepos")
    #xbmc.executebuiltin("UpdateLocalAddons")
    #xbmc.Monitor().waitForAbort(10)
    updateManager.forceRepoUpdate(0)
    xbmc.Monitor().waitForAbort(10)
    updateManager.forceRepoUpdate(1)
    updateState = updateManager.isUpdate()
    if(updateState):
        dialog.notification('xPress', 'Update konnte nicht installiert werden, bitte versuchen Sie es in ein paar Minuten erneut', xbmcgui.NOTIFICATION_WARNING, 5000, True)
    else:
        dialog.notification('xPress', 'Erfolgreich aktualisiert', xbmcgui.NOTIFICATION_INFO, 5000, True)
elif(updateState) == False:
    updateManager.forceRepoUpdate(1)
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 5000, True)
else:
    dialog.notification('xPress', 'Updateprozess wurde abgebrochen, siehe Details: kodi.log', xbmcgui.NOTIFICATION_ERROR, 5000, True)


