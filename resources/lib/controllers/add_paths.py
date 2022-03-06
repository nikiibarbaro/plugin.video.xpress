import xbmcaddon
import xbmcvfs
from sys import path
from os.path import join
import os

global ADDON_NAME
ADDON_NAME = "plugin.video.xpress"

global addonPath
addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))

global pathAddonDataAddon
pathAddonDataAddon = xbmcvfs.translatePath(
    join("special://home", "userdata", "addon_data", "{0}".format(ADDON_NAME)))

os.makedirs(pathAddonDataAddon, exist_ok=True)
global pathAddonSettings
pathAddonSettings = xbmcvfs.translatePath(join(pathAddonDataAddon, "settings.json"))

path.append(addonPath)
path.append(join(addonPath, "art"))
path.append(join(addonPath, "resources", "lib", "modules"))
path.append(join(addonPath, "resources", "lib", "models"))
path.append(join(addonPath, "resources", "lib", "sites"))
path.append(join(addonPath, "resources", "lib", "views"))
path.append(join(addonPath, "resources", "lib", "controllers"))
