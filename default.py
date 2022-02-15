# -*- coding: utf-8 -*-

import sys, xbmc, xbmcgui
import resolveurl as resolver
#import urlresolver as resolver

sLink = resolver.resolve("https://anicloud.io/redirect/775490")
xbmc.executebuiltin("PlayMedia("+sLink+")")
