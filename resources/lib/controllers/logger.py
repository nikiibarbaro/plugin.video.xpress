import xbmc
import sys
import os

from resources.lib.controllers.addon_add_global_variables import ADDON_ID


class Logger:
    """Class for log events"""

    def __init__(self, file: str):
        self.file = file

    def debug(self, message: str):
        """To see debug you need to enable Settings/System/Logging/Enable debug logging"""
        xbmc.log(ADDON_ID + "::" + self.file + " - " + message,
                 xbmc.LOGDEBUG)

    def info(self, message: str):
        xbmc.log(ADDON_ID + "::" + self.file + " - " + message,
                 xbmc.LOGINFO)

    def warning(self, message: str):
        xbmc.log(ADDON_ID + "::" + self.file + " - " + message,
                 xbmc.LOGWARNING)

    def error(self, message: str):
        xbmc.log(ADDON_ID + "::" + self.file + " - " + message,
                 xbmc.LOGERROR)

    def fatal(self, message: str):
        xbmc.log(ADDON_ID + "::" + self.file + " - " + message,
                 xbmc.LOGFATAL)
