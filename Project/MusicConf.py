from NoteConf import *

from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *


from lylib import *

class Music:

    _m_RunMusic = False

    _m_CurrentSongTitle = None
    _m_PlayingSong = None
    _m_CurrentNote = None

    _m_CurrentSongBPM = None

    def __init__(self,Songname):
        self._m_CurrentSongTitle=Songname
        self._loadsong()
        Mbox("Music Conf", "init music conf \n%s" % Songname,0)



    def _loadsong(self):
        if SearchFile(self._m_CurrentSongTitle):
            Mbox("Find Song", "%s"%self._m_CurrentSongTitle, 0)

        self._m_PlayingSong = Mix_LoadMUS('Resources\\Song\\evens.mp3')

        self._m_CurrentNote = Note._notesync(1, self._m_CurrentSongTitle)

Music =Music('11')

Music._loadsong()