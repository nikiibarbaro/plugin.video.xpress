import xbmcgui
import xbmc
import xbmcvfs
import xbmcaddon
import requests
import re
from os.path import join
from sys import path
#from packaging import version

#import pydevd
#pydevd.settrace('localhost', port=1234, stdoutToServer=True, stderrToServer=True)
#import web_pdb;
#web_pdb.set_trace()

test1 = 'plugin.video.xpress'
test2= xbmcaddon.Addon(test1)
test3 = xbmcvfs.translatePath(test2.getAddonInfo('path'))
path.append(test3)
path.append(join(test3, "resources", "lib", "modules"))
from packaging import version

"""
    USER = Username
    REPOSITORY_NAME = Repository name
    ADDON_NAME = Addon name
    ADDON_PATH = Addon path
"""
USER = "nikiibarbaro"
REPOSITORY_NAME = "repository.xpress"
ADDON_NAME = "plugin.video.xpress"
ADDON_PATH = "zips/plugin.video.xpress"

"""special protocol variable for multi OS support"""
pathHome = xbmcvfs.translatePath("special://home")
pathXbmc = xbmcvfs.translatePath("special://xbmc")
pathAddon = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("path")

"""
    Stopping addon just for safty to not conflict with potential updates
"""
xbmc.executebuiltin("StopScript(addon)")

"""
    Get .zip from zips/plugin.video.xpress, only works with one .zip 
    file existing in subdirectory (maybe later adding support for multiple .zips but for now it works as expected)
"""
url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(USER, REPOSITORY_NAME)
response = requests.get(url)
responseData = response.json()
for structure_tree in responseData["tree"]:
    if(structure_tree["path"]==ADDON_PATH):
        url = str(structure_tree["url"])
        break
response = requests.get(url)
responseData = response.json()
for structure_tree in responseData["tree"]:
    teste = str(structure_tree["path"])
    if (re.search("plugin.video.xpress-{1}.*.zip{1}",str(structure_tree["path"]))):
        addonFilenameZip = structure_tree["path"]
        break

"""Get version from .zip"""
addonVersionRemote = re.search("plugin.video.xpress-(.*).zip",addonFilenameZip).group(1)

"""Get version from local addon"""
addonVersionLocal = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("version")

"""Create dialog object for displaying informations"""
dialog = xbmcgui.Dialog()

"""Check versions"""
if (version.parse(addonVersionRemote) > version.parse(addonVersionLocal)):
    dialog.notification('xPress', 'Ein neues Update ist verfügbar', xbmcgui.NOTIFICATION_INFO, 5000, True)
else:
    dialog.notification('xPress', 'Keine neuen Updates verfügbar', xbmcgui.NOTIFICATION_INFO, 5000, True)


"""Get url to .zip in zips/plugin.video.xpress"""
url = "https://github.com/{}/{}/blob/master/zips/{}/{}?raw=true".format(USER, REPOSITORY_NAME, ADDON_NAME, addonFilenameZip)

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
