import json
import add_paths
import os.path


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


class Settings:

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

    @staticmethod
    def getIsUpdated():
        with open(add_paths.pathAddonSettings) as json_file:
            data = json.load(json_file)
        if(data["settings"][0]["isUpdated"]==True):
            return True
        else:
            return False
