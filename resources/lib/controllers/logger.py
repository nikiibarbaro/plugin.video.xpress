import xbmc
import sys

ADDON_NAME = "plugin.video.xpress"


class Logger:

    def __init__(self):
        pass

    @staticmethod
    def debug(message):
        xbmc.log("[" + ADDON_NAME + "]: " + message,
                 xbmc.LOGDEBUG)

    @staticmethod
    def info(message):
        xbmc.log("[" + ADDON_NAME + "]: " + message,
                 xbmc.LOGINFO)

    @staticmethod
    def warning(message):
        xbmc.log("[" + ADDON_NAME + "]: " + message,
                 xbmc.LOGWARNING)

    @staticmethod
    def error(message):
        xbmc.log("[" + ADDON_NAME + "]: " + message,
                 xbmc.LOGERROR)

    @staticmethod
    def fatal(message):
        xbmc.log("[" + ADDON_NAME + "]: " + message,
                 xbmc.LOGFATAL)
