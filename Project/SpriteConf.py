from pico2d import *
from lylib import *

import TimerConf

class Sprite:

    def __init__(self):
        #self.Timer = TimerConf.Timer()
        self.SpriteFrame = 0
        self._m_CurrentTime = 0.0
        self._m_PrevTime = 0.0

        self._m_SpriteAccTime = 0.0

    def SpriteTimer(self, Currenttime, Prevtime):
        self._m_CurrentTime = Currenttime
        self._m_PrevTime = Prevtime
        self._m_SpriteAccTime += self._m_CurrentTime - self._m_PrevTime
        if self._m_SpriteAccTime > 0.02:
            self.SpriteFrame = (self.SpriteFrame + 1) % 10
            self._m_SpriteAccTime -= 0.02

            print('spritetimercall', self.SpriteFrame)

