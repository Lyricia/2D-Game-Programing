from lylib import *

import MusicConf
import PlayScene
import MenuScene
import SpriteConf
import InputManager

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
    def event_handler(self):        # not in progress, should separate to 'input manager'
        events=get_events()

        for event in events:
            if event.type == SDL_QUIT:
                self._m_State=False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self._m_State=False
                if event.key == SDLK_q:
                    self._m_State = False
                if event.key == SDLK_s:
                    if self._m_runMusic == False :
                        self._m_runMusic = True
                        self._m_musicname = '120BPM'
                        self._m_CurrentScene = 'PlayScene'
                if event.key == SDLK_d:
                    if self._m_runMusic == False:
                        self._m_runMusic = True
                        self._m_musicname = 'Evans'
                        self._m_CurrentScene = 'PlayScene'
                if event.key == SDLK_a:
                    if self._m_runMusic == False:
                        self._m_runMusic = True
                        self._m_musicname = '180BPM'
                        self._m_CurrentScene = 'PlayScene'

                if event.key == SDLK_m:
                    if self._m_runMusic == True:
                        self._m_Music.MusicStop()
                        del(self._m_Music)
                        self._m_runMusic = False
                        self._m_CurrentScene = 'MenuScene'

                if self._m_runMusic:
                    if event.key == SDLK_e :
                        #self._m_Music._m_CurrentNote.UpdateNote()
                        self._m_Music._m_CurrentNote.notejudgechk()
                        self._m_SpriteTimer[0].bSprite = True
                    if event.key == SDLK_r :
                        self._m_Music._m_CurrentNote.notejudgechk()
                        self._m_SpriteTimer[1].bSprite = True
                    if event.key == SDLK_u:
                        self._m_Music._m_CurrentNote.notejudgechk()
                        self._m_SpriteTimer[2].bSprite = True
                    if event.key == SDLK_i :
                        self._m_Music._m_CurrentNote.notejudgechk()
                        self._m_SpriteTimer[3].bSprite = True


                if self._m_runMusic and self._m_Music:
                    if event.key == SDLK_1 and self._m_Music._m_CurrentNote._m_speed != 1:
                        self._m_Music._m_CurrentNote._m_speed = 1
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_2 and self._m_Music._m_CurrentNote._m_speed != 2:
                        self._m_Music._m_CurrentNote._m_speed = 2
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_3 and self._m_Music._m_CurrentNote._m_speed != 3:
                        self._m_Music._m_CurrentNote._m_speed = 3
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_4 and self._m_Music._m_CurrentNote._m_speed != 4:
                        self._m_Music._m_CurrentNote._m_speed = 4
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_5 and self._m_Music._m_CurrentNote._m_speed != 5:
                        self._m_Music._m_CurrentNote._m_speed = 5
                        self._m_Music._m_CurrentNote._NotePosition()

                if event.key is SDLK_z:
                    print('z')
                if event.key is SDLK_x:
                    print('x')
                if event.key is SDLK_c:
                    print('c')

    def event(self):
        self.keys = SDL_GetKeyboardState(None)

        self.bKeyDown = False

        if self.keys[SDL_SCANCODE_S]:
            if self._m_runMusic == False:
                self._m_runMusic = True
                self._m_musicname = '120BPM'
                self._m_CurrentScene = 'PlayScene'

        if self._m_runMusic:
            if self.keys[SDL_SCANCODE_E] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(0)
                self._m_SpriteTimer[0].bSprite = True
            if self.keys[SDL_SCANCODE_R] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(1)
                self._m_SpriteTimer[1].bSprite = True
            if self.keys[SDL_SCANCODE_U] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(2)
                self._m_SpriteTimer[2].bSprite = True
            if self.keys[SDL_SCANCODE_I] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(3)
                self._m_SpriteTimer[3].bSprite = True

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
        self._m_InputManager = InputManager.InputManager()
        self._m_CurrentScene = 'MenuScene'

    def _update(self):
        self.event()
        #self._m_InputManager.event()
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
        if self._m_CurrentScene:
           self._scenesetup()
           self._m_CurrentScene.sceneupdate()
        else:
            pass
        update_canvas()

    def _scenesetup(self):
        if self._m_CurrentScene == 'PlayScene':
            self._m_SpriteTimer = list()
            for idx in range(0, 4):
                self._m_SpriteTimer.append(SpriteConf.Sprite())
            self._m_CurrentScene = PlayScene.PlayScene(self._m_Music, self._m_SpriteTimer)
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