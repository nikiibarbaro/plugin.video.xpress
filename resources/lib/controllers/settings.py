import json
from resources.lib.controllers.addon_add_paths import pathAddonSettings
import os.path

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

"""Class for settings used in addon"""


class Settings:
    """Sets state of 'isUpdated'"""

    @staticmethod
    def setIsUpdated(state):
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

    """Gets state of 'isUpdated'"""

    @staticmethod
    def getIsUpdated():
        with open(pathAddonSettings) as json_file:
            data = json.load(json_file)
        if (data["settings"][0]["isUpdated"] == "True"):
            Settings.setIsUpdated(False)
            return True
        else:
            return False
