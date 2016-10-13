from lylib import *

#Loading Note Data & return Note Date list

class Note:

    _m_speed = 1
    _m_keynum = 4
    _m_judgeidx = 0
    _m_ElapsedVal = 0
    _m_CurrentNoteIdx = 0

    notechk = 0

    def __init__(self, Songname, SongBPM):
        self._m_Notelist = list()
        self._notesync(Songname)

        self._m_speed = 1
        self._m_SongBPM = int(SongBPM)
        self._m_judgeidx = 0
        self._m_posacctime = 0
        self._m_idxacctime = 0

        self._NotePosition()
        self._m_ElapsedVal = 0

        self._m_CurrentNoteIdx = 0

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

        self._NotePosition()

        print("notename \n%s" % Songname)
        return self._m_Notelist #note Loading end -> return to song conf

    def _NotePosition(self):
        for keyidx in range(self._m_keynum):
            for idx in range(len(self._m_Notelist[0])):
                if self._m_Notelist[keyidx][idx] != 0:
                    self._m_Notelist[keyidx][idx] = 159 \
                                                    + (40 * idx * self._m_speed) \
                                                    - (40 * self._m_CurrentNoteIdx * self._m_speed) \
                                                    - int(self._m_ElapsedVal)

    def UpdateNote(self):
        for keyidx in range(self._m_keynum):
            for tmp in range(len(self._m_Notelist[0])):
                if self._m_Notelist[keyidx][tmp] > 126 - 1 * self._m_speed:
                    self._m_Notelist[keyidx][tmp] -= 1

    def NoteTimer(self, prevtime, currenttime):
        self._m_idxacctime += currenttime - prevtime
        self._m_posacctime += currenttime - prevtime
        if self._m_idxacctime > 60.0 / float(self._m_SongBPM):
            self._m_CurrentNoteIdx += 1
            self._m_idxacctime -= 60.0 / float(self._m_SongBPM)
            for idx in range(self._m_keynum):
             self._m_Notelist[idx][self._m_CurrentNoteIdx] = 0
        if self._m_posacctime > 1 / float(self._m_SongBPM) / self._m_speed:
            self.UpdateNote()
            self._m_posacctime -= 1 / float(self._m_SongBPM) / self._m_speed



    def notejudgechk(self):
        idx = self._m_judgeidx
        while idx < len(self._m_Notelist[0]):
            if self._m_Notelist[0][idx] != 0 and self._m_Notelist[0][idx] > 135 and self._m_Notelist[0][idx] <169:
                print('Pass')

        pass