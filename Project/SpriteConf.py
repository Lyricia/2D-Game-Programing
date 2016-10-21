class Sprite:

    def __init__(self):
        #self.Timer = TimerConf.Timer()
        self.SpriteFrame = 0
        self._m_CurrentTime = 0.0
        self._m_PrevTime = 0.0
        self._m_SpriteFrameTime = 0.015
        self._m_SpriteAccTime = 0.0
        self.bSprite = False

    def SpriteTimer(self, Currenttime, Prevtime):
        if self.bSprite:
            self._m_CurrentTime = Currenttime
            self._m_PrevTime = Prevtime
            self._m_SpriteAccTime += self._m_CurrentTime - self._m_PrevTime
            if self._m_SpriteAccTime > self._m_SpriteFrameTime:
                self.SpriteFrame = self.SpriteFrame + 1
                self._m_SpriteAccTime -= self._m_SpriteFrameTime
            if self.SpriteFrame > 25:
                self.bSprite = False
                self.SpriteFrame = 0