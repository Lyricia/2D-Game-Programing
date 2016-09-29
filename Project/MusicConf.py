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
    _m_PlayEndTime = None

    _m_CurrentNote = None
    _m_CurrentSongBPM = None

    def __init__(self,Songname):

        music_f=open('Resources\\Song\\song list.txt')
        for line in music_f:
             line = line.split(' ')
            if line[0] == Songname:
                self._m_CurrentSongTitle = line[1]
                self._m_CurrentNote = line[2]
                self._m_CurrentSongBPM = line[3]
                self._m_PlayEndTime = datetime.time() + datetime.timedelta(line[4]) + 5
                pass


        self._m_CurrentSongTitle=Songname
        self._loadsong()
        Mbox("Music Conf", "init music conf \n%s" % Songname,0)



    def _loadsong(self):
        if SearchFile(self._m_CurrentSongTitle):
            Mbox("Find Song", "%s"%self._m_CurrentSongTitle, 0)
            self._m_PlayingSong = load_music('Resources\\Song\\evans.ogg')
            #self._m_PlayEndTime = time.time() +
            self._m_CurrentNote = Note._notesync(0,self._m_CurrentSongTitle)

            if self._m_CurrentNote:
                pass

            self._m_PlayingSong.set_volume(60)
            self._m_PlayingSong.play()




    def MusicFinished(self,Time_now):           #if time now passed music during time return stop (True)
        if Time_now > self._m_PlayEndTime + 3:
            return True

music = Music('Evans')