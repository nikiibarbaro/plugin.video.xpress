import xbmcaddon
import xbmc
import requests  # normal to be not recognized by IDEA due packages not exists in env
import re
import os
import xml.etree.ElementTree as et

# import web_pdb;#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
# web_pdb.set_trace()#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
from resources.lib.models.addon_add_global_variables import ADDON_ID, USER, REPOSITORY_NAME, ADDON_PATH

"""Add filepath from imports to addon"""
from resources.lib.modules.packaging import version
from resources.lib.models.settings import Settings
from resources.lib.models.logger import Logger

"""Create logger"""
logger = Logger(os.path.basename(__file__))


class updateManager:
    """Class for handling updates"""

    @staticmethod
    def getLocalVersion():
        """Gets version from local addon"""
        try:
            addonVersionLocal = xbmcaddon.Addon(ADDON_ID).getAddonInfo("version")
            logger.setDebugLog("Local version: " + addonVersionLocal)
        except RuntimeError:
            logger.setDebugLog("Local version couldn't be fetched")
            xbmc.sleep(4000)
            addonVersionLocal = xbmcaddon.Addon(ADDON_ID).getAddonInfo("version")
        if (addonVersionLocal is None):
            logger.setDebugLog("Local version is None")
            return None
        return addonVersionLocal

    @staticmethod
    def getRemoteVersion():
        """Gets version from remote zip"""
        url = "https://raw.githubusercontent.com/{0}/{1}/master/zips/addons.xml".format(USER, REPOSITORY_NAME)
        response = requests.get(url)
        if (response.status_code != 200):
            logger.setDebugLog("Couldn't get response")
            return None
        tree = et.fromstring(response.content)
        for element in tree:
            if (element.attrib.get("id") == ADDON_ID):
                remoteVersion = element.attrib.get("version")
                logger.setDebugLog("Remote version: " + remoteVersion)
                return remoteVersion
        logger.setDebugLog("Couldn't fetch remote version")
        return None

    @staticmethod
    def forceRepoUpdate():
        """forces Kodi to check for new updates in the Repo and installing it"""
        logger.setDebugLog("Force update")
        xbmc.executebuiltin("UpdateAddonRepos")

    @staticmethod
    def isUpdate():
        """Checks if update is available"""
        remoteVersion = updateManager.getRemoteVersion()
        localVersion = updateManager.getLocalVersion()
        if (remoteVersion is None or localVersion is None):
            return None
        if (version.parse(remoteVersion) > version.parse(localVersion)):
            logger.setDebugLog("New update is available")
            logger.setDebugLog("Old version: " + localVersion)
            logger.setDebugLog("New version: " + remoteVersion)
            return True
        else:
            logger.setDebugLog("Addon is up to date")
            return False

    @staticmethod
    def getIsUpdated():
        """Gets state whether on last run an update was applied to addon"""
        logger.setDebugLog("Gets getIsUpdated state")
        return Settings.getIsUpdated()

    @staticmethod
    def setIsUpdated(state):
        """Sets state of json 'isUpdated' to True/False"""
        logger.setDebugLog("Sets setIsUpdated state: " + state)
        Settings.setIsUpdated(state)

    @staticmethod
    def enableAddon():
        """Enables addon"""
        logger.setDebugLog("Addon enabled")
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":true}}' % ADDON_ID)

    @staticmethod
    def disableAddon():
        """Disables addon"""
        logger.setDebugLog("Addon disabled")
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":false}}' % ADDON_ID)

    @staticmethod
    def getLatestFilename():
        """Crawls through jsons to get the latest zip filename"""
        addonFilenameZip = ''
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

    @staticmethod
    def getLatestZipUrl():
        """Gets url to .zip in zips/plugin.video.xpress"""
        addonFilenameZip = updateManager.getLatestFilename()
        if (addonFilenameZip is None):
            return None
        url = "https://github.com/{0}/{1}/blob/master/zips/{2}/{3}?raw=true".format(USER, REPOSITORY_NAME, ADDON_ID,
                                                                                    addonFilenameZip)
        return url
