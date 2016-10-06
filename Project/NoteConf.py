from lylib import *

#Loading Note Data & return Note Date list

class Note:

    m_Notelist = None

    def __init__(self, Songname):
        self._notesync(Songname)
        self.m_Notelist = []


    def _notesync(self, Songname):
        f = open("Resources\\Note\\%s" %Songname, 'r')
        Notelist = f.readlines()
        for idx in range(len(Notelist)):
            Notelist = list(Notelist[idx])

            pass
        f.close()

        Mbox("note test", "notename \n%s" % Songname, 0)

        return Notelist #note Loading end -> return to song conf


note = Note('Evans.txt')
