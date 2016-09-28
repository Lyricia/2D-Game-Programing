from lylib import *

#Loading Note Data & return Note Date list

class Note:

    def __init__(self):
        self._notesync("evans")

    def _notesync(self, Songname):
        f = open("Resources\\Note\\%s" %Songname + '.txt', 'r')
        Notelist = f.readlines()
        for line in Notelist:
            print(line)
        f.close()

        Mbox("note test", "notename \n%s" % Songname, 0)

        return Notelist #note Loading end -> return to song conf