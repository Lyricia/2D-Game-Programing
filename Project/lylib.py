from pico2d import *
from sdl2 import *
from sdl2.sdlmixer import *

import ctypes  # An included library with Python install.
import os
import time



def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)




def SearchFile(target):
    targetsong = target + '.mp3'
    targetnote = target + '.txt'
    rootdir = os.getcwd()
    musicdir = rootdir + '\\Resources\\Song'
    notedir = rootdir + '\\Resources\\Note'

    print(rootdir)
    print(musicdir)
    print(notedir)

    musiclist = os.listdir(musicdir)
    notelist = os.listdir(notedir)

    if targetsong in musiclist:
        if targetnote in notelist:
            return True
        else:
            Mbox("CANNOT FIND NOTEFILE", "CANNOT FIND NOTEFILE\n %s\nPlz Chk Note dir" % targetnote, 0)
    else:
        Mbox("CANNOT FIND SONG", "CANNOT FIND SONG\n %s\nPlz Chk Music dir" % targetsong, 0)
        return False

