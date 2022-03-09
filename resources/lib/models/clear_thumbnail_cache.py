import sqlite3
import re
from os.path import join
import xbmcvfs

from resources.lib.models.addon_add_paths import pathThumbnails, pathAddonDatabase

class clearThumbnailCache:
    """
    Clears thumbnail cache in Kodi for a specific addon
    """

    @staticmethod
    def start():

        conn = sqlite3.connect(join(pathAddonDatabase, "Textures13.db"))
        r = conn.cursor()

        r.execute('SELECT * FROM texture')
        table = r.fetchall()

        """Gets all files which not include http but xpress and repository"""
        for elem in table:
            if (re.findall("^(?!.*http).*(plugin.video.xpress|repository.xpress).*", elem[1])):
                path = join(pathThumbnails, elem[2])
                xbmcvfs.delete(path)
        conn.close()
