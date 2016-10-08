from lylib import *

import MusicConf
import PlayScene
import Menu

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

    def event_handler(self):
        events=get_events()

        for event in events:
            if event.type == SDL_QUIT:
                self._m_State=False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self._m_State=False
                elif event.key == SDLK_q:
                    self._m_State = False
                elif event.key == SDLK_s:
                    self._m_runMusic = True
                    self._m_CurrentScene = 'PlayScene'
                elif event.key == SDLK_m:
                    self._m_runMusic = False
                    self._m_CurrentScene = 'Menu'
                    self._m_Music.MusicStop()
                    self._m_Music = None


    def _create(self):
        open_canvas(800,760)
        self._m_CurrentScene = 'Menu'



    def _update(self):
        self.event_handler()
        if self._m_runMusic == True:
            if self._m_Music == None:
                self._m_Music = MusicConf.Music('Evans')
            elif self._m_Music:
                self._m_Music._m_CurrentNote.UpdateNote(self._m_AccTime)

            if self._m_Music.MusicFinished():
                print("end")
                self._m_runMusic=None
                self._m_Music=None
                self._m_CurrentScene = 'Menu'



    def _draw(self):
        if self._m_CurrentScene:
           self._scenesetup()
           self._m_CurrentScene.sceneupdate()
        pass

    def _scenesetup(self):
        if self._m_CurrentScene == 'PlayScene':
            self._m_CurrentScene = PlayScene.PlayScene(self._m_Music)
        if self._m_CurrentScene == 'Menu':
            self._m_CurrentScene = Menu.MenuScene()



    def run(self):
        self._create()
        self._m_State=True
        while self._m_State:
            self._m_CurrentTime = time.time()
            self._m_AccTime += self._m_CurrentTime - self._m_PrevTime
            self._m_PrevTime = self._m_CurrentTime
            if self._m_AccTime > self._m_FPS_MAX:       # draw when fps over
                self._update()
                self._draw()
                self._m_AccTime = 0

        self._exit()


    def _exit(self):
        self._m_State=False