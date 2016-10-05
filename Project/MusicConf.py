from NoteConf import *

from lylib import *

class Music:

    _m_RunMusic = False

    CurrentSongTitle = None
    _m_PlayingSong = None
    _m_PlayEndTime = None

    _m_CurrentNote = None
    _m_CurrentSongBPM = None

    def __init__(self,Songname):
        if searchfile(Songname):
            Mbox("Find Song", "%s"%Songname, 0)

            music_f=open('Resources\\Song\\song list.txt')
            for line in music_f:
                line = line.split(' ')
                if line[0] == Songname:
                    self._m_CurrentSongTitle = line[1]
                    self._m_CurrentNote = line[2]
                    self._m_CurrentSongBPM = line[3]
                    self._m_PlayEndTime = time.time() + float(10) + float(2)
                    break

            self._loadsong()

            Mbox("Music Conf", "init music conf \n%s" % Songname,0)


    def _loadsong(self):

        self._m_PlayingSong = load_music('Resources\\Song\\%s' %self._m_CurrentSongTitle)
        self._m_CurrentNote = Note(self._m_CurrentNote)
        self._m_PlayingSong.set_volume(60)
        self._m_PlayingSong.play()


    def MusicStop(self):
        self._m_PlayingSong.stop()


    def MusicFinished(self):           #if time now passed music during time return stop (True)
        currenttime=time.time()

        if currenttime > self._m_PlayEndTime:
            return True