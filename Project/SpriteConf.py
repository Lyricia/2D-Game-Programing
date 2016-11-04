class Sprite:

    def __init__(self, spritename = 'effect'):
        #self.Timer = TimerConf.Timer()
        self.spritename = spritename
        self.SpriteFrame = 0
        self.SpriteFramelimit = 0
        self._m_CurrentTime = 0.0
        self._m_PrevTime = 0.0
        self._m_SpriteFrameTime = 0.015
        self._m_SpriteAccTime = 0.0
        self.bSprite = False
        self.framelock = False

    def SpriteTimer(self, Currenttime, Prevtime):
        if self.spritename is 'keysprite':
            self.SpriteFramelimit = 7
            self._m_SpriteFrameTime = 0.025
        elif self.spritename is 'effect':
            self.SpriteFramelimit = 25
            self._m_SpriteFrameTime = 0.015

        if self.bSprite:
            self._m_CurrentTime = Currenttime
            self._m_PrevTime = Prevtime
            self._m_SpriteAccTime += self._m_CurrentTime - self._m_PrevTime
            if self._m_SpriteAccTime > self._m_SpriteFrameTime:
                self.SpriteFrame = self.SpriteFrame + 1
                self._m_SpriteAccTime -= self._m_SpriteFrameTime
            if self.SpriteFrame > self.SpriteFramelimit:
                self.bSprite = False
                self.SpriteFrame = 0


