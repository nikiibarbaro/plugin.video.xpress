import xbmcgui
import xbmc
import xbmcaddon
import xbmcvfs
from os.path import join
from sys import path

from os.path import join
from sys import path

ADDON_NAME = "plugin.video.xpress"
#import pydevd
#pydevd.settrace('localhost', port=1234, stdoutToServer=True, stderrToServer=True)
import web_pdb;
web_pdb.set_trace()

addonXpress = xbmcaddon.Addon(ADDON_NAME)
xpressAddonPath = xbmcvfs.translatePath(addonXpress.getAddonInfo('path'))
path.append(xpressAddonPath)
path.append(join(xpressAddonPath, "resources", "lib", "utils"))
from resources.lib.utils.updateManager import updateManager

"""
    Stopping addon just for safty to not conflict with potential updates
"""
xbmc.executebuiltin("StopScript(addon)")

"""Create dialog object for displaying informations"""
dialog = xbmcgui.Dialog()

test = updateManager.isUpdate()
if (test is None):
    dialog.notification('xPress', 'Ein Fehler beim Updateprozess trat auf', xbmcgui.NOTIFICATION_INFO, 5000, True)
elif (test):
    dialog.notification('xPress', 'Ein neues Update wurde gefunden', xbmcgui.NOTIFICATION_INFO, 5000, True)
else:
    dialog.notification('xPress', 'Keine neuen Updates gefunden', xbmcgui.NOTIFICATION_INFO, 5000, True)

updateManager.disableAddon()
dialog.notification('xPress', 'Test', xbmcgui.NOTIFICATION_INFO, 5000, True)
dialog.notification('xPress', 'Test', xbmcgui.NOTIFICATION_INFO, 5000, True)
dialog.notification('xPress', 'Test', xbmcgui.NOTIFICATION_INFO, 5000, True)
updateManager.enableAddon()
"""Download .zip file"""
# response = requests.get(url, stream=True)
# with open('E:\\test.zip', 'wb') as fd:
#     for chunk in response.iter_content(chunk_size=512):
#         fd.write(chunk)
#
#
#
#
# dialog.ok('', url)
#
#
# dialog.notification('xPress', 'Add-on wurde erfolgreich geupdated', xbmcgui.NOTIFICATION_INFO, 5000, True)
