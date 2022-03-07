import xbmcgui
import xbmc
import xbmcaddon
import xbmcvfs

from os.path import join
from sys import path

ADDON_NAME = "plugin.video.xpress"

import web_pdb;  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
web_pdb.set_trace()  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

# addonXpress = xbmcaddon.Addon(ADDON_NAME)
# xpressAddonPath = xbmcvfs.translatePath(addonXpress.getAddonInfo('path'))
# path.append(xpressAddonPath)
# path.append(join(xpressAddonPath, "resources", "lib", "controllers"))


addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
path.append(join(addonPath, "resources", "lib", "controllers"))

from resources.lib.controllers.update_manager import updateManager
import resources.lib.controllers.add_paths
from resources.lib.controllers.settings import Settings
from resources.lib.controllers.logger import Logger

"""
    Stopping addon just for safty to not conflict with potential updates
"""
# xbmc.executebuiltin("StopScript(addon)")

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
    Settings.setIsUpdated(True)
    updateManager.forceRepoUpdate()
elif (updateState) == False:
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 2000, True)
else:
    dialog.notification('xPress', 'Updateprozess wurde abgebrochen, siehe Details: kodi.log',
                        xbmcgui.NOTIFICATION_ERROR, 5000, True)
