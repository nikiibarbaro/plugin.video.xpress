import json
import add_paths
import os.path

"""Initialize json structure on first use"""
if not (os.path.exists(add_paths.pathAddonSettings)):
    structure = {
        "settings": [
            {
                "isUpdated": "false"
            }
        ]
    }

    initJson = json.dumps(structure)
    with open(add_paths.pathAddonSettings, "w+") as settings:
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
        with open(add_paths.pathAddonSettings, "w+") as settings:
            settings.write(settingsJson)

    """Gets state of 'isUpdated'"""

    @staticmethod
    def getIsUpdated():
        with open(add_paths.pathAddonSettings) as json_file:
            data = json.load(json_file)
        if (data["settings"][0]["isUpdated"] == True):
            Settings.setIsUpdated(False)
            return True
        else:
            return False
