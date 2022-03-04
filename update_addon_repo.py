import xbmc
import xbmcgui

ADDON_ID = "plugin.video.xpress"
dialog = xbmcgui.Dialog()
dialog.notification('xPress', 'Ein neues Update ist verfügbar und wird installiert', xbmcgui.NOTIFICATION_INFO, 5000, True)
xbmc.executebuiltin("StopScript({0})".format(ADDON_ID))
xbmc.executebuiltin("UpdateAddonRepos")
xbmc.executebuiltin("UpdateLocalAddons")
#xbmc.sleep(5000)
dialog.notification('xPress', 'Erfolgreich aktualisiert', xbmcgui.NOTIFICATION_INFO, 5000, True)
