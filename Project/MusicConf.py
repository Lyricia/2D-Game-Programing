from NoteConf import *

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
            Mbox("Find", "Find", 0)

        #self._m_PlayingSong=load_music(self._m_CurrentSongTitle)

        self._m_CurrentNote = Note._notesync(1, self._m_CurrentSongTitle)

