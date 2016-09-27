from pico2d import *

import ctypes  # An included library with Python install.
import os



def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)




def SearchFile(targetsong):
    rootdir=os.getcwd()
    musicdir = rootdir+'\\Resources\\Song'
    notedir = rootdir+'\\Resources\\Note'

    print(rootdir)
    print(musicdir)
    print(notedir)

    musiclist=os.listdir(musicdir)
    filenames=os.listdir(notedir)

    if targetsong in musiclist:
        return True
    else:
        Mbox("CANNOT FIND SONG", "CANNOT FIND SONG\n %s\nPlz Chk Resource\Music" %targetsong,0)
        return False

