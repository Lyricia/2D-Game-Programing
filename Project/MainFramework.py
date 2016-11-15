from lylib import *

import PlayScene
import MenuScene
import GameOverScene
import ResultScene
import PlayerConf

class Framework:

    _m_State = False

    #Frame
    _m_FPS_MAX = 1/60

    _m_CurrentTime = 0.0
    _m_PrevTime = 0.0
    _m_AccTime = 0.0           #Accumulated time -> playing time

    #music
    _m_Music = None
    _m_runMusic = False
    _m_CurrentScene = None

    _m_NoteData = None

    _m_KeySpriteTimer = None
    _m_EffectSpriteTimer = None
    _m_isPaused = False

    _m_musicname = None

    _m_player = None

    def handle_event(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self._m_State = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self._m_State = False
                if event.key == SDLK_q:
                    self._m_State = False

    def _create(self):
        open_canvas(800, 760)
        self._m_CurrentScene = 'MenuScene'
        self._m_player = PlayerConf.player()
        self.switchscene(self._m_CurrentScene)

    def _update(self):
        self.handle_event()
        if self._m_CurrentScene is not None:
            self._m_CurrentScene.sceneupdate()
            pass

    def _draw(self):
        clear_canvas()
        if self._m_CurrentScene is not None:
            self._m_CurrentScene.scenedraw()
        update_canvas()

    def switchscene(self, Scenename):
        self._m_CurrentScene = Scenename
        if self._m_CurrentScene == 'PlayScene':
            self._m_CurrentScene = PlayScene.PlayScene(self, self._m_musicname)
        if self._m_CurrentScene == 'MenuScene':
            self._m_CurrentScene = MenuScene.MenuScene(self)
        if self._m_CurrentScene == 'GameOverScene':
            self._m_CurrentScene = GameOverScene.GameOverScene(self)
        if self._m_CurrentScene == 'ResultScene':
            self._m_CurrentScene = ResultScene.ResultScene(self)


    def run(self):
        self._create()
        self._m_State=True
        self._m_PrevTime = time.time()
        while self._m_State:
            self._m_CurrentTime = time.time()
            self._m_AccTime += self._m_CurrentTime - self._m_PrevTime

            if self._m_NoteData is not None:
                if self._m_isPaused is False:
                    self._m_NoteData.NoteTimer(self._m_CurrentTime, self._m_PrevTime)

            for idx in range(0,4):
                if self._m_KeySpriteTimer is not None:
                    if self._m_KeySpriteTimer[idx].bSprite:
                        self._m_KeySpriteTimer[idx].SpriteTimer(self._m_CurrentTime, self._m_PrevTime)
                if self._m_EffectSpriteTimer is not None:
                    if self._m_EffectSpriteTimer[idx].bSprite:
                        self._m_EffectSpriteTimer[idx].SpriteTimer(self._m_CurrentTime, self._m_PrevTime)

            self._m_PrevTime = self._m_CurrentTime


            if self._m_AccTime > self._m_FPS_MAX:       # draw when time over fps
                self._update()
                self._draw()
                self._m_AccTime -= self._m_FPS_MAX

        self._exit()


    def _exit(self):
        self._m_State=False