import xbmcaddon
import xbmcvfs
from sys import path
from os.path import join

ADDON_NAME = "plugin.video.xpress"

addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))

class addPaths:
    """Append paths"""
    path.append(addonPath)
    path.append(join(addonPath, "resources", "lib", "modules"))
    path.append(join(addonPath, "resources", "lib", "models"))
    path.append(join(addonPath, "resources", "lib", "sites"))
    path.append(join(addonPath, "resources", "lib", "views"))