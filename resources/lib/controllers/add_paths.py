import xbmcaddon
import xbmcvfs
from sys import path
from os.path import join
import os

"""
MAKE SURE TO IMPORT THIS FILE FIRST IN THE ROOT FILE TO ENSURE PROPER USE!
File to set global variables and path appends to ensure the addon knows all the paths being used in classes
"""

"""Sets addon name for global use"""
global ADDON_NAME
ADDON_NAME = "plugin.video.xpress"

"""Sets translated path from the addon location"""
global addonPath
addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))

"""Sets translated path from the addon_data/addon location"""
global pathAddonDataAddon
pathAddonDataAddon = xbmcvfs.translatePath(
    join("special://home", "userdata", "addon_data", "{0}".format(ADDON_NAME)))

"""Creates recursive dirs for addon_data/addon location"""
os.makedirs(pathAddonDataAddon, exist_ok=True)

"""Sets translated path from the settings.json location"""
global pathAddonSettings
pathAddonSettings = xbmcvfs.translatePath(join(pathAddonDataAddon, "settings.json"))

"""Appends various paths used in the addon"""
path.append(addonPath)
path.append(join(addonPath, "art"))
path.append(join(addonPath, "resources", "lib", "modules"))
path.append(join(addonPath, "resources", "lib", "models"))
path.append(join(addonPath, "resources", "lib", "sites"))
path.append(join(addonPath, "resources", "lib", "views"))
path.append(join(addonPath, "resources", "lib", "controllers"))
