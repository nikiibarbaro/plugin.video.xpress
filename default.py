# -*- coding: utf-8 -*-

import sys, xbmc, xbmcgui, xbmcaddon, xbmcvfs
from sys import path
import web_pdb;
web_pdb.set_trace()
resolverAddonID = 'script.module.resolveurl'
resolverAddon= xbmcaddon.Addon(resolverAddonID)
addonResolverTranslatedPath = xbmcvfs.translatePath(resolverAddon.getAddonInfo('path'))

path.append(addonResolverTranslatedPath)

import resolveurl as resolver
#import urlresolver as resolver

sLink = resolver.resolve('https://voe.sx/e/y0a379ohxuj5')
xbmc.Player(sLink)
