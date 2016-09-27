from lylib import *

class Note:

    def __init__(self):
        self._notesync("testsong")

    def _notesync(self, Songname):
        Mbox("note test", "notename \n%s" % Songname, 0)