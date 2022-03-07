import xbmcaddon
import xbmcvfs
from sys import path
from os.path import join
import os
from resources.lib.controllers.addon_add_global_variables import ADDON_ID

"""
MAKE SURE TO IMPORT THIS FILE FIRST IN THE ROOT FILE TO ENSURE PROPER USE!
File to set global variables and path appends to ensure the addon knows all the paths being used in classes
"""

"""Sets translated path from the addon location"""
global addonPath
addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_ID).getAddonInfo('path'))

"""Sets translated path from the addon_data/addon location"""
global pathAddonDataAddon
pathAddonDataAddon = xbmcvfs.translatePath(
    join("special://home", "userdata", "addon_data", "{0}".format(ADDON_ID)))

"""Creates recursive dirs for addon_data/addon location"""
os.makedirs(pathAddonDataAddon, exist_ok=True)

"""Sets translated path from the settings.json location"""
global pathAddonSettings
pathAddonSettings = xbmcvfs.translatePath(join(pathAddonDataAddon, "settings.json"))

global pathPackages
pathPackages = xbmcvfs.translatePath(join("special://home", "addons", "packages"))

global pathHome
pathHome = xbmcvfs.translatePath("special://home")

global pathXbmc
pathXbmc = xbmcvfs.translatePath("special://xbmc")

"""Appends various paths used in the addon"""
path.append(addonPath)
path.append(pathAddonDataAddon)
path.append(pathAddonSettings)
path.append(pathPackages)
path.append(pathHome)
path.append(pathXbmc)
path.append(join(addonPath, "art"))
path.append(join(addonPath, "resources", "lib", "modules"))
path.append(join(addonPath, "resources", "lib", "models"))
path.append(join(addonPath, "resources", "lib", "sites"))
path.append(join(addonPath, "resources", "lib", "views"))
path.append(join(addonPath, "resources", "lib", "controllers"))

from resources.lib.controllers.logger import Logger

"""Create logger"""
logger = Logger(os.path.basename(__file__))

logger.debug("Paths appended")
