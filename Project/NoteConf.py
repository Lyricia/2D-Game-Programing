from lylib import *

#Loading Note Data & return Note Date list

class Note:

    _m_Notelist = list()

    _m_SongDuration = None
    _m_SongBPM = 0
    _m_PlayingTime = 0.0
    _m_Updateidx = 0

    _m_CallNote = 0

    def __init__(self, Songname, SongDuration, SongBPM):
        self._notesync(Songname)
        self._m_SongDuration = int(SongDuration)
        self._m_SongBPM = int(SongBPM)
        self._m_CallNote = round(self._m_SongBPM / 60 * 10)


    def _notesync(self, Songname):
        f = open("Resources\\Note\\%s" %Songname, 'r')
        Notelist = f.readlines()
        for idx in range(len(Notelist)):
            tmp = list(Notelist[idx])
            self._m_Notelist.append(tmp)
            pass

        f.close()

        Mbox("note test", "notename \n%s" % Songname, 0)

        return self._m_Notelist #note Loading end -> return to song conf


    def UpdateNote(self, Acctime):

        self._m_PlayingTime += Acctime

        if self._m_PlayingTime > 10 * self._m_Updateidx:
            for idx in range(self._m_CallNote):
                if self._m_Notelist[0][idx + self._m_CallNote * self._m_Updateidx] == '1':
                    self._m_Notelist[0][idx + self._m_CallNote * self._m_Updateidx] = 760 + 60 * idx

            self._m_Updateidx += 1

        for idx in range(self._m_CallNote):
            if self._m_Notelist[0][idx] != '0':
                self._m_Notelist[0][idx] -= self._m_SongBPM / 60 * 5
                if self._m_Notelist[0][idx] < 0:
                    self._m_Notelist[0][idx] == '0'






        print(self._m_PlayingTime)
        pass