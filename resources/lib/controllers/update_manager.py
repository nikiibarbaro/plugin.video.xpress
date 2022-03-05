import xbmcaddon
import xbmcvfs
import xbmc
import requests  # normal to be not recognized by IDEA due packages not exists in env
import re
import os
import sqlite3
import datetime
import xml.etree.ElementTree as et

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
pathPackages = xbmcvfs.translatePath(join("special://home", "addons", "packages"))
pathDatabase = xbmcvfs.translatePath(join("special://home", "userdata", "Database", "Addons33.db"))
# pathAddon = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("path")

"""Add filepath from imports to addon"""
# addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
# path.append(join(addonPath, "resources", "lib", "controllers"))
# addonPath = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_NAME).getAddonInfo('path'))
# xpressAddonPath = xbmcvfs.translatePath(addonXpress.getAddonInfo('path'))
# path.append(addonPath)
# path.append(join(addonPath, "resources", "lib", "modules"))
# from resources.lib.controllers.addPaths import addPaths
from resources.lib.modules.packaging import version


class updateManager:
    """Get version from local addon"""

    @staticmethod
    def getLocalVersion():
        try:
            addonVersionLocal = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("version")
        except RuntimeError:
            xbmc.sleep(4000)
            addonVersionLocal = xbmcaddon.Addon(ADDON_NAME).getAddonInfo("version")
        if (addonVersionLocal is None):
            return None
        return addonVersionLocal

    """Get version from remote zip"""

    @staticmethod
    def getRemoteVersion():
        url = "https://raw.githubusercontent.com/{0}/{1}/master/zips/addons.xml".format(USER, REPOSITORY_NAME)
        response = requests.get(url)
        if (response.status_code != 200):
            return None
        tree = et.fromstring(response.content)
        for element in tree:
            if (element.attrib.get("id") == ADDON_NAME):
                remoteVersion = element.attrib.get("version")
                return remoteVersion
        return None

    @staticmethod
    def forceRepoUpdate():


        connection = sqlite3.connect(pathDatabase)
        action = connection.cursor()

        # Update on startup
        nextUpdate = updateManager.setUpdateInterval(updateManager.getGlobalTime(), interval_h=0, interval_m=0,interval_s=1)
        action.execute('UPDATE repo SET nextcheck = "{0}" WHERE addonID ="repository.xpress"'.format(nextUpdate))
        connection.commit()
        action.execute('SELECT nextcheck FROM repo WHERE addonID ="repository.xpress"')
        updateStart = action.fetchone()
        xbmc.sleep(2000)
        # Update after 8 hours default time
        nextUpdate = updateManager.setUpdateInterval(updateManager.getGlobalTime())
        action.execute('UPDATE repo SET nextcheck = "{0}" WHERE addonID ="repository.xpress"'.format(nextUpdate))
        connection.commit()
        action.execute('SELECT nextcheck FROM repo WHERE addonID ="repository.xpress"')
        updateHours = action.fetchone()

        connection.close()

    @staticmethod
    def setUpdateInterval(timestamp, interval_h=8, interval_m=0, interval_s=0):
        timestamp = ''.join(timestamp)
        nextUpdate = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=interval_h,
                                                                                                     minutes=interval_m,
                                                                                                     seconds=interval_s)
        return str(nextUpdate)

    @staticmethod
    def getGlobalTime():
        globalTime = datetime.datetime.now()
        return str(globalTime.strftime("%Y-%m-%d %H:%M:%S"))

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
        url = "https://github.com/{0}/{1}/blob/master/zips/{2}/{3}?raw=true".format(USER, REPOSITORY_NAME, ADDON_NAME,
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
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":true}}' % ADDON_NAME)

    """Disable Addon"""

    @staticmethod
    def disableAddon():
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":false}}' % ADDON_NAME)

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
        if (os.path.isfile(pathPackages + "\\{0}".format(filename))):
            os.remove(pathPackages + "\\{0}".format(filename))
        else:
            print("Error: %s file not found" % pathPackages + "\\{0}".format(filename))

# """Download latest version as .zip file"""
# @staticmethod
# def update(self):
#     url = self.getLatestZipUrl()
#     response = requests.get(url, stream=True)
#     with open('E:\\test.zip', 'wb') as fd:
#         for chunk in response.iter_content(chunk_size=512):
#             fd.write(chunk)
