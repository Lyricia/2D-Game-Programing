from lylib import *

import MusicConf
import PlayScene
import MenuScene
import SpriteConf

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
    _m_SpriteTimer = None
    _m_CurrentScene = None

    _m_musicname = None

    def handle_event(self):
        self.keys = SDL_GetKeyboardState(None)

        self.bKeyDown = False

        if self.keys[SDL_SCANCODE_S]:
            if self._m_runMusic == False:
                self._m_runMusic = True
                self._m_musicname = '120BPM'
                self._m_CurrentScene = 'PlayScene'

        if self.keys[SDL_SCANCODE_D]:
            if self._m_runMusic == False:
                self._m_runMusic = True
                self._m_musicname = 'Evans'
                self._m_CurrentScene = 'PlayScene'

        if self.keys[SDL_SCANCODE_A]:
            if self._m_runMusic == False:
                self._m_runMusic = True
                self._m_musicname = '180BPM'
                self._m_CurrentScene = 'PlayScene'



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
        open_canvas(800,760)
        self._m_CurrentScene = 'MenuScene'

    def _update(self):
        self.handle_event()
        if self._m_runMusic == True:
            if self._m_Music == None:
                self._m_Music = MusicConf.Music(self._m_musicname)
            if self._m_Music.MusicFinished():
                print("end")
                self._m_Music.MusicStop()
                del (self._m_Music)
                self._m_runMusic = False
                self._m_CurrentScene = 'MenuScene'

    def _draw(self):
        clear_canvas()
        if self._m_CurrentScene is not None:
            self.switchscene(self._m_CurrentScene)
            self._m_CurrentScene.sceneupdate()
        else:
            pass
        update_canvas()

    def switchscene(self, Scenename):
        self._m_CurrentScene = Scenename
        if self._m_CurrentScene == 'PlayScene':
            self._m_SpriteTimer = list()
            for idx in range(0, 4):
                self._m_SpriteTimer.append(SpriteConf.Sprite())
            self._m_CurrentScene = PlayScene.PlayScene(self._m_Music, self._m_SpriteTimer, self)
        if self._m_CurrentScene == 'MenuScene':
            self._m_CurrentScene = MenuScene.MenuScene()


    def run(self):
        self._create()
        self._m_State=True
        self._m_PrevTime = time.time()
        while self._m_State:
            self._m_CurrentTime = time.time()
            if self._m_Music is not None:
                self._m_Music._m_CurrentNote.NoteTimer(self._m_CurrentTime, self._m_PrevTime)

            if self._m_SpriteTimer is not None:
                for idx in range(0,4):
                    if self._m_SpriteTimer[idx].bSprite:
                        self._m_SpriteTimer[idx].SpriteTimer(self._m_CurrentTime, self._m_PrevTime)

            self._m_AccTime += self._m_CurrentTime - self._m_PrevTime
            self._m_PrevTime = self._m_CurrentTime
            if self._m_AccTime > self._m_FPS_MAX:       # draw when time over fps
                self._update()
                self._draw()
                self._m_AccTime -= self._m_FPS_MAX

        self._exit()


    def _exit(self):
        self._m_State=False