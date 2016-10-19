from lylib import *

class Timer :

    def __init__(self):
        self._m_CurrentTime = 0.0
        self._m_PrevTime = 0.0

        self._m_SpriteAccTime = 0.0
        pass

    def __del__(self):
        pass

    def _TimerUpdate(self):
        self._m_PrevTime = time.time()
        self._m_CurrentTime = time.time()

    def SpriteTimeUpdate(self):
        self._TimerUpdate()
        self._m_SpriteAccTime += self._m_CurrentTime - self._m_PrevTime
        if self._m_SpriteAccTime > 0.02:
            self._m_SpriteAccTime -= 0.02
            return True
        else: return False
