"""
MAKE SURE TO IMPORT THIS FILE FIRST IN THE ROOT FILE TO ENSURE PROPER USE!
File to set global variables and path appends to ensure the addon knows all the paths being used in classes
"""
import os
from resources.lib.controllers.logger import Logger


"""Create logger"""
logger = Logger(os.path.basename(__file__))

global ADDON_ID
ADDON_ID = "plugin.video.xpress"

global USER
USER = "nikiibarbaro"

global REPOSITORY_NAME
REPOSITORY_NAME = "repository.xpress"

global ADDON_PATH
ADDON_PATH = "zips/plugin.video.xpress"

logger.debug("Global variables created")
