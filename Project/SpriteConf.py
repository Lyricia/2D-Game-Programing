from pico2d import *
from lylib import *

import TimerConf

class Sprite:

    def __init__(self):
        self.Timer = TimerConf.Timer()
        self.SpriteFrame = 0

    def SpriteTimer(self):
        if self.Timer.SpriteTimeUpdate():
            self.SpriteFrame = (self.SpriteFrame + 1) % 10
            print(self.SpriteFrame)

