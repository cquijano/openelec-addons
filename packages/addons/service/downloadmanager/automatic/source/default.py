################################################################################
################################################################################

import os
import sys
import xbmcaddon
import time
import subprocess

__scriptname__ = "Automatic torrent dowloader"
__author__ = "Carlos Quijano"
__url__ = "http://kylek.is-a-geek.org:31337/"
__settings__   = xbmcaddon.Addon(id='service.downloadmanager.automatic')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, 'bin', "automatic.start") )
__stop__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "automatic.stop") )

#make binary files executable in adson bin folder
subprocess.Popen("chmod -R +x " + __cwd__ + "/bin/*" , shell=True, close_fds=True)

subprocess.Popen(__start__, shell=True, close_fds=True)

while (not xbmc.abortRequested):
  time.sleep(0.250)

subprocess.Popen(__stop__, shell=True, close_fds=True)

