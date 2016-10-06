from lylib import *

#Loading Note Data & return Note Date list

class Note:

    _m_Notelist = list()

    def __init__(self, Songname):
        self._notesync(Songname)


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