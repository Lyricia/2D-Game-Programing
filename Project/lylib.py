from pico2d import *
from math import *

import ctypes  # An included library with Python install.
import os
import datetime
import time



def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def searchfile(target):
    targetsong = target + '.mp3'
    targetnote = target + '.txt'
    rootdir = os.getcwd()
    musicdir = rootdir + '\\Resources\\Song'
    notedir = rootdir + '\\Resources\\Note'

    musiclist = os.listdir(musicdir)
    notelist = os.listdir(notedir)

    if targetsong in musiclist:
        if targetnote in notelist:
            return True
        else:
            Mbox("CANNOT FIND NOTEFILE", "CANNOT FIND NOTEFILE\n %s\nPlz Chk Note dir" % targetnote, 0)
            return False
    else:
        Mbox("CANNOT FIND SONG", "CANNOT FIND SONG\n %s\nPlz Chk Music dir" % targetsong, 0)
        return False
