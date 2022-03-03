import xbmcaddon
import xbmcvfs
import xbmc
import requests #normal to be not recognized by IDEA due packages not exists in env
import re
import os

from os.path import join
from sys import path

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
pathPackages = xbmcvfs.translatePath(join("special://home","addons", "packages"))
#pathAddon = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("path")

"""Add filepath from imports to addon"""
#addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
#path.append(join(addonPath, "resources", "lib", "controllers"))
#addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
#xpressAddonPath = xbmcvfs.translatePath(addonXpress.getAddonInfo('path'))
#path.append(addonPath)
#path.append(join(addonPath, "resources", "lib", "modules"))
#from resources.lib.controllers.addPaths import addPaths
from resources.lib.modules.packaging import version


class updateManager:
    """Get version from local addon"""

    @staticmethod
    def getLocalVersion():
        addonVersionLocal = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("version")
        if (addonVersionLocal is None):
            return None
        return addonVersionLocal

    """Get version from remote zip"""

    @staticmethod
    def getRemoteVersion():
        addonFilenameZip = updateManager.getLatestFilename()
        if (addonFilenameZip is None):
            return None
        addonVersionRemote = re.search("plugin.video.xpress-(.*).zip", addonFilenameZip).group(1)
        return addonVersionRemote

    """This function crawls through jsons to get the latest zip filename"""

    @staticmethod
    def getLatestFilename():
        try:
            url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(USER, REPOSITORY_NAME)
            response = requests.get(url)
            responseData = response.json()
            for structure_tree in responseData["tree"]:
                if (structure_tree["path"] == ADDON_PATH):
                    url = str(structure_tree["url"])
                    break
            response = requests.get(url)
            responseData = response.json()
            for structure_tree in responseData["tree"]:
                teste = str(structure_tree["path"])
                if (re.search("plugin.video.xpress-{1}.*.zip{1}", str(structure_tree["path"]))):
                    addonFilenameZip = structure_tree["path"]
                    break
        except BaseException:
            return None
        else:
            return addonFilenameZip

    """Get url to .zip in zips/plugin.video.xpress"""

    @staticmethod
    def getLatestZipUrl():
        addonFilenameZip = updateManager.getLatestFilename()
        if (addonFilenameZip is None):
            return None
        url = "https://github.com/{}/{}/blob/master/zips/{}/{}?raw=true".format(USER, REPOSITORY_NAME, ADDON_NAME,
                                                                                addonFilenameZip)
        return url

    """Checks if update is available"""
    @staticmethod
    def isUpdate():
        remoteVersion = updateManager.getRemoteVersion()
        localVersion = updateManager.getLocalVersion()
        if (remoteVersion is None or localVersion is None):
            return None
        if (version.parse(remoteVersion) > version.parse(localVersion)):
            return True
        else:
            return False

    """Enable Addon"""
    @staticmethod
    def enableAddon():
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":true}}' % ADDON_NAME)

    """Disable Addon"""
    @staticmethod
    def disableAddon():
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":false}}' % ADDON_NAME)

    """Checks if addon.zip in packages exist"""
    @staticmethod
    def getCachedPackageName():
        arr = os.listdir(pathPackages)
        for name in arr:
            if (re.search("plugin.video.xpress-{1}.*.zip{1}", name)):
                return name
        return None

    """Remove cached addon.zip"""
    @staticmethod
    def clearCachedPackage():
        filename = updateManager.getCachedPackageName()
        if (os.path.isfile(pathPackages+"\\{}".format(filename))):
            os.remove(pathPackages+"\\{}".format(filename))
        else:
            print("Error: %s file not found" % pathPackages+"\\{}".format(filename))


# """Download latest version as .zip file"""
# @staticmethod
# def update(self):
#     url = self.getLatestZipUrl()
#     response = requests.get(url, stream=True)
#     with open('E:\\test.zip', 'wb') as fd:
#         for chunk in response.iter_content(chunk_size=512):
#             fd.write(chunk)