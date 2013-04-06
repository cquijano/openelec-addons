################################################################################
################################################################################

import os
import sys
import xbmcaddon
import time
import subprocess

__scriptname__ = "Automatic program that keep free space on hard disk"
__author__ = "Carlos Quijano"
__url__ = ""
__settings__   = xbmcaddon.Addon(id='service.downloadmanager.deleter')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, 'bin', "deleter.start") )
__stop__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "deleter.stop") )

#make binary files executable in adson bin folder
subprocess.Popen("chmod -R +x " + __cwd__ + "/bin/*" , shell=True, close_fds=True)

subprocess.Popen(__start__, shell=True, close_fds=True)

while (not xbmc.abortRequested):
  time.sleep(0.250)

subprocess.Popen(__stop__, shell=True, close_fds=True)

