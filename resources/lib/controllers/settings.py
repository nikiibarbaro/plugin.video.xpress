import json
from resources.lib.controllers.addon_add_paths import pathAddonSettings
from resources.lib.controllers.logger import Logger
import os.path

"""Create logger"""
logger = Logger(os.path.basename(__file__))

"""Initialize json structure on first use"""
if not (os.path.exists(pathAddonSettings)):
    structure = {
        "settings": [
            {
                "isUpdated": "false"
            }
        ]
    }

    initJson = json.dumps(structure)
    with open(pathAddonSettings, "w+") as settings:
        settings.write(initJson)
    logger.debug("Init json was written with default values")


class Settings:
    """Class for settings used in addon"""

    @staticmethod
    def setIsUpdated(state):
        """Sets state of 'isUpdated'"""
        settings = {
            "settings": [
                {
                    "isUpdated": "{}".format(state)
                }
            ]
        }
        settingsJson = json.dumps(settings)
        with open(pathAddonSettings, "w+") as settings:
            settings.write(settingsJson)
        logger.debug("State of isUpdated was updated to: " + state)

    @staticmethod
    def getIsUpdated():
        """Gets state of 'isUpdated'"""
        with open(pathAddonSettings) as json_file:
            data = json.load(json_file)
        if (data["settings"][0]["isUpdated"] == "True"):
            Settings.setIsUpdated(False)
            return True
        else:
            return False
