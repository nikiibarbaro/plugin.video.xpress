import xbmcaddon
import xbmc
import requests  # normal to be not recognized by IDEA due packages not exists in env
import re
import xml.etree.ElementTree as et


# import web_pdb;#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
# web_pdb.set_trace()#NEED TO COMMENTED OUT BEFORE PUSHING TO GITHUB TO PREVENT UPDATER BREAKS
from resources.lib.controllers.addon_add_global_variables import ADDON_ID, USER, REPOSITORY_NAME, ADDON_PATH

"""Add filepath from imports to addon"""
from resources.lib.modules.packaging import version
from resources.lib.controllers.settings import Settings


class updateManager:
    """Gets version from local addon"""

    @staticmethod
    def getLocalVersion():
        try:
            addonVersionLocal = xbmcaddon.Addon(ADDON_ID).getAddonInfo("version")
        except RuntimeError:
            xbmc.sleep(4000)
            addonVersionLocal = xbmcaddon.Addon(ADDON_ID).getAddonInfo("version")
        if (addonVersionLocal is None):
            return None
        return addonVersionLocal

    """Gets version from remote zip"""

    @staticmethod
    def getRemoteVersion():
        url = "https://raw.githubusercontent.com/{0}/{1}/master/zips/addons.xml".format(USER, REPOSITORY_NAME)
        response = requests.get(url)
        if (response.status_code != 200):
            return None
        tree = et.fromstring(response.content)
        for element in tree:
            if (element.attrib.get("id") == ADDON_ID):
                remoteVersion = element.attrib.get("version")
                return remoteVersion
        return None

    """forces Kodi to check for new updates in the Repo and installing it"""

    @staticmethod
    def forceRepoUpdate():
        xbmc.executebuiltin("UpdateAddonRepos")

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

    """Gets state whether on last run an update was applied to addon"""

    @staticmethod
    def getIsUpdated():
        return Settings.getIsUpdated()

    """Sets state of json 'isUpdated' to True/False"""

    @staticmethod
    def setIsUpdated(state):
        Settings.setIsUpdated(state)

    """Enables addon"""

    @staticmethod
    def enableAddon():
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":true}}' % ADDON_ID)

    """Disables addon"""

    @staticmethod
    def disableAddon():
        xbmc.executeJSONRPC(
            '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid":"%s", "enabled":false}}' % ADDON_ID)

    """Crawls through jsons to get the latest zip filename"""

    @staticmethod
    def getLatestFilename():
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

    """Gets url to .zip in zips/plugin.video.xpress"""

    @staticmethod
    def getLatestZipUrl():
        addonFilenameZip = updateManager.getLatestFilename()
        if (addonFilenameZip is None):
            return None
        url = "https://github.com/{0}/{1}/blob/master/zips/{2}/{3}?raw=true".format(USER, REPOSITORY_NAME, ADDON_ID,
                                                                                    addonFilenameZip)
        return url
