from lylib import *

import SpriteConf


#Loading Note Data & return Note Date list

class Note:

    _m_speed = 1
    _m_keynum = 4
    _m_judgeidx = 0
    _m_ElapsedVal = 0
    _m_CurrentNoteIdx = 0
    _m_calljudgeSpriteTimer = None

    notechk = 0

    def __init__(self, Songname, SongBPM):
        self._m_Notelist = list()
        self._notesync(Songname)

        self._m_speed = 1
        self._m_SongBPM = int(SongBPM)
        self._m_posacctime = 0
        self._m_idxacctime = 0

        self._NotePosition()
        self._m_ElapsedVal = 0

        self._m_CurrentNoteIdx = 0
        self._m_calljudgeSpriteTimer = SpriteConf.Sprite()

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
                    self._m_Notelist[keyidx][idx] = (float)(159 \
                                                    + (60 * idx * self._m_speed) \
                                                    - (60 * self._m_CurrentNoteIdx * self._m_speed) \
                                                    + self._m_ElapsedVal)

    def UpdateNote(self):
        for keyidx in range(self._m_keynum):
            for tmp in range(len(self._m_Notelist[0])):
                if self._m_Notelist[keyidx][tmp] > 10 - 1 * self._m_speed and self._m_Notelist[keyidx][tmp] != 0:
                    self._m_Notelist[keyidx][tmp] -= 1 * self._m_speed
                    self._m_ElapsedVal = (self._m_ElapsedVal + 1 * self._m_speed) % (60 * self._m_speed)
                    #print(self._m_ElapsedVal)
                if self._m_Notelist[keyidx][tmp] < 126:
                    self._m_Notelist[keyidx][tmp] = 0



    def NoteTimer(self, currenttime, prevtime):
        self._m_idxacctime += currenttime - prevtime
        self._m_posacctime += currenttime - prevtime

        if self._m_idxacctime > 60.0 / float(self._m_SongBPM):      #timer to count Current Beat Note Index
            self._m_CurrentNoteIdx += 1
            self._m_idxacctime -= 60.0 / float(self._m_SongBPM)

        if self._m_posacctime > 1 / float(self._m_SongBPM):         #Timer Move note 1 pixel per 1/BPM sec
            self.UpdateNote()
            self._m_posacctime -= 1 / float(self._m_SongBPM)




    def notejudgechk(self,keynum):
        for idx in range(len(self._m_Notelist[0])):
            if 125 < self._m_Notelist[keynum][idx] < 175:
                print('pass')
                self._m_Notelist[keynum][idx] = 0

    def __del__(self):
        del self._m_Notelist