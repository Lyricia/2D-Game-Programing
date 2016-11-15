from NoteConf import *

from lylib import *

class Music:

    _m_CurrentNote = None
    _m_CurrentSongTitle = None

    _m_PlayingSong = None

    _m_PlayEndTime = None
    _m_SongDuration = None

    _m_CurrentSongBPM = None

    def __init__(self,Songname):
        if searchfile(Songname):
            print("Find song : %s" % Songname)

            music_f=open('Resources\\Song\\song list.txt')
            for line in music_f:
                line = line.split(' ')
                if line[0] == Songname:
                    self._m_CurrentSongTitle = line[1]
                    self._m_CurrentNote = line[2]
                    self._m_CurrentSongBPM = line[3]
                    self._m_SongDuration = line[4]
                    self._m_StartTime = time.time()
                    self._m_PlayEndTime = self._m_StartTime  + float(self._m_SongDuration) + float(0.5)
                    break

            self._loadsong()


            print("init music conf \n%s" % Songname)


    def _loadsong(self):

        self._m_PlayingSong = load_music('Resources\\Song\\%s' %self._m_CurrentSongTitle)
        self._m_CurrentNote = Note(self._m_CurrentNote, self._m_CurrentSongBPM)
        self._m_PlayingSong.set_volume(80)
        self._m_PlayingSong.play()

    def MusicPause(self):
        self._m_PlayingSong.pause()

    def MusicResume(self):
        self._m_PlayingSong.resume()

    def MusicStop(self):
        self._m_PlayingSong.stop()

    def MusicFinished(self):           #if time now passed music during time return stop (True)
        currenttime=time.time()
        if currenttime > self._m_PlayEndTime:
            return True

    def __del__(self):
        del(self._m_CurrentNote)
        del(self._m_CurrentSongTitle)
        del(self._m_PlayingSong)
        del(self._m_PlayEndTime)
        del(self._m_SongDuration)
        del(self._m_CurrentSongBPM)
