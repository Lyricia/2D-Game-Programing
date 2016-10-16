from pico2d import *
from lylib import *

class Sprite:

    def __init__(self):
        self._m_CurrentTime = 0
        self._m_PrevTime = 0
        self._m_AccTime = 0
        self._m_SpriteFrame =0

    def SpriteTimer(self):
        self._m_PrevTime = time.time()
        self._m_CurrentTime = time.time()
        self._m_AccTime += self._m_CurrentTime - self._m_PrevTime
        if self._m_AccTime > 0.02:
            self._m_SpriteFrame += 1
            self._m_AccTime -= 0.02
            print(self._m_SpriteFrame)