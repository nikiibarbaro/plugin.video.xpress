# -*- coding: utf-8 -*-

import sys, xbmc, xbmcgui
import resolveurl as resolver
#import urlresolver as resolver

sLink = resolver.resolve(str('https://voe.sx/e/q71l8ub1kp3b'))
xbmc.executebuiltin('PlayMedia('+sLink+')')
