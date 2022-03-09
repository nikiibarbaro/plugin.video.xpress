import os
from resources.lib.models.logger import Logger


class LoggerController:

    def __init__(self, file):
        """
        Creates a logger object

        :param file: os.path.basename(__file__)
        """
        logger = Logger(os.path.basename(__file__))

    def setDebugLog(self, message: str):
        Logger.setDebugLog(message)

    def setInfoLog(self, message: str):
        Logger.setInfoLog(message)

    def setWarningLog(self, message: str):
        Logger.setWarningLog(message)

    def setErrorLog(self, message: str):
        Logger.setErrorLog(message)

    def setFatalLog(self, message: str):
        Logger.setFatalLog(message)