from lylib import *

#Loading Note Data & return Note Date list

class Note:

    _m_speed = 1
    _m_keynum = 4
    _m_judgeidx = 0

    def __init__(self, Songname, SongDuration, SongBPM):
        self._m_Notelist = list()
        self._notesync(Songname)
        self._m_speed = 1
        self._m_SongBPM = int(SongBPM)
        self._m_judgeidx = 0
        self._m_acctime = 0

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

        f.close()

        self._NotePosition(0)

        print("notename \n%s" % Songname)
        return self._m_Notelist #note Loading end -> return to song conf


    def _NotePosition(self, runmusic):
        if not runmusic:
            for keyidx in range(self._m_keynum):
                for idx in range(len(self._m_Notelist[0])):
                    if self._m_Notelist[keyidx][idx] != 0:
                        self._m_Notelist[keyidx][idx] = 760 + 40 * idx * self._m_speed * self._m_speed + 40 * self._m_speed * self._m_speed
        if runmusic:
            for keyidx in range(self._m_keynum):
                for idx in range(len(self._m_Notelist[0])):
                    if self._m_Notelist[keyidx][idx] != 0:
                        self._m_Notelist[keyidx][idx] = 40 * idx * self._m_speed * self._m_speed + 40 * self._m_speed * self._m_speed



    def UpdateNote(self, Acctime):


        self._m_acctime += Acctime
        if self._m_acctime > self._m_SongBPM / 3600:
            for keyidx in range(self._m_keynum):
                for tmp in range(len(self._m_Notelist[0])):  # while tmp < self._m_CallNote * self._m_Updateidx:
                    if self._m_Notelist[keyidx][tmp] != 0:
                        self._m_Notelist[keyidx][tmp] -= 10 * self._m_speed
                        print(self._m_Notelist[keyidx][tmp], tmp)
                    tmp += 1
                for idx in range(len(self._m_Notelist[keyidx])):
                    if int(self._m_Notelist[keyidx][idx]) < 140:
                        self._m_Notelist[keyidx][idx] = 0
                        self._m_judgeidx += 1

        #print(self._m_PlayingTime)


        pass


    def notejudgechk(self):
        idx = self._m_judgeidx
        while idx < len(self._m_Notelist[0]):
            if self._m_Notelist[0][idx] != 0 and self._m_Notelist[0][idx] > 135 and self._m_Notelist[0][idx] <169:
                print('Pass')

        pass