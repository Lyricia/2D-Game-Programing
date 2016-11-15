from lylib import *

import json


class player:
    def __init__(self,name='Player01'):
        self.keynum = 4
        self.name = name
        self.fever = 0
        self.score = 0
        self.avgacc = 0
        self.rank = 0
        pass

    def savestat(self):
        f = open('Save\\%s.txt' % self.name, 'w')
        json.dump([self.name, self.keynum, self.score, self.rank], f)
        f.close()
        pass

    def loadstat(self):
        if searchfile(self.name,True):
            f=open('Save\\%s.txt' % self.name, 'r')
            [self.name, self.keynum, self.score, self.rank] = json.load(f)
            f.close()
        else:
            print('Cannot find savefile\n')

    def setStat(self, _score, _avgacc):
        self.avgacc = _avgacc
        self.score = _score