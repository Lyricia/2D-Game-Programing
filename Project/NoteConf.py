from lylib import *

#Loading Note Data & return Note Date list

class Note:

    _m_Notelist = list()

    _m_SongDuration = None
    _m_SongBPM = 0

    _m_PlayingTime = 0.0
    _m_Updateidx = 0
    _m_speed = 1
    _m_keynum = 4

    _m_CallNote = 0

    def __init__(self, Songname, SongDuration, SongBPM):
        self._notesync(Songname)
        self._m_speed = 4
        self._m_SongDuration = int(SongDuration)
        self._m_SongBPM = int(SongBPM)
        self._m_CallNote = round(self._m_SongBPM / 60 * 5)

        self._m_acctime = 0
        self.notedropidx = 0

        self._NotePosition(0)

    def _notesync(self, Songname):
        f = open("Resources\\Note\\%s" %Songname, 'r')
        Notelist = f.readlines()
        for idx in range(len(Notelist)):
            tmp = list(Notelist[idx])
            if tmp[-1]=='\n':
                tmp.remove('\n')
            tmp = list(map(int,tmp))
            self._m_Notelist.append(tmp)
            pass

        f.close()

        print("notename \n%s" % Songname)

        return self._m_Notelist #note Loading end -> return to song conf

    def _NotePosition(self, Acctime):
        #self._m_PlayingTime += Acctime

        #if self._m_PlayingTime > 5 * self._m_Updateidx:
        #    for keyidx in range(self._m_keynum):
        #        for idx in range(self._m_CallNote):
        #            if self._m_Notelist[keyidx][idx + self._m_CallNote * self._m_Updateidx] != 0:
        #                self._m_Notelist[keyidx][idx + self._m_CallNote * self._m_Updateidx] = 760 + 40 * idx * self._m_speed
        #    self._m_Updateidx += 1

        for keyidx in range(self._m_keynum):
            for idx in range(len(self._m_Notelist[0])):
                if self._m_Notelist[keyidx][idx] != 0:
                    self._m_Notelist[keyidx][idx] = 760

    def UpdateNote(self, Acctime):

        #self._NotePosition(Acctime)
        #
        #for keyidx in range(self._m_keynum):
        #    for tmp in range(self._m_CallNote * self._m_Updateidx):         #while tmp < self._m_CallNote * self._m_Updateidx:
        #        if self._m_Notelist[keyidx][tmp] != 0:
        #            self._m_Notelist[keyidx][tmp] -= self._m_SongBPM * self._m_speed * 2 / 3 * Acctime
        #            print(self._m_Notelist[keyidx][tmp] , tmp)
        #        tmp += 1
        #
        #    for idx in range(len(self._m_Notelist[keyidx])):
        #        if int(self._m_Notelist[keyidx][idx]) < 0:
        #            self._m_Notelist[keyidx][idx] = 0
        #
        #print(self._m_PlayingTime)

        self._m_acctime += Acctime
        if self._m_acctime > 1/60 * self._m_SongBPM / 60:
            self._m_acctime = 0.0
            self.notedropidx += 1

        for idx in range(self.notedropidx):
            self._m_Notelist[0][idx] -= (40 / self._m_SongBPM) * 20 * self._m_speed

    def notejudgechk(self):
        if self._m_Notelist[0]:
            pass

        pass