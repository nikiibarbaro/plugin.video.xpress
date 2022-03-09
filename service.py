"""Kodi builtin imports"""
import xbmcgui
import xbmc

import os

"""Debugging"""
# import web_pdb;  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

"""Execute debugging"""
# web_pdb.set_trace()  # NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS

"""Required imports, appends controllers to sys.path in order that Kodi can import addon_add_paths.py"""
#from resources.lib.controllers import addon_add_paths
#from resources.lib.controllers import addon_add_global_variables

"""Required imports"""
from resources.lib.controllers.update_manager import updateManager
from resources.lib.models.logger import Logger
from resources.lib.models.clear_thumbnail_cache import clearThumbnailCache

"""Create logger"""
logger = Logger(os.path.basename(__file__))

"""Create dialog object for displaying informations"""
dialog = xbmcgui.Dialog()
clearThumbnailCache.start()
if (updateManager.getIsUpdated()):
    dialog.notification('xPress', 'Erfolgreich aktualisiert', xbmcgui.NOTIFICATION_INFO,
                        2000, True)
    xbmc.sleep(2000)
updateState = updateManager.isUpdate()
if (updateState):
    dialog.notification('xPress', 'Ein neues Update ist verfügbar und wird installiert', xbmcgui.NOTIFICATION_INFO,
                        2000, True)
    updateManager.setIsUpdated("True")
    updateManager.forceRepoUpdate()
elif (updateState) == False:
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 2000, True)
else:
    dialog.notification('xPress', 'Updateprozess wurde abgebrochen, siehe Details: kodi.log',
                        xbmcgui.NOTIFICATION_ERROR, 5000, True)
