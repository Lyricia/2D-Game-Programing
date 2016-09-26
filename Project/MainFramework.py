from pico2d import *

import time
import MusicConf

class Framework:

    _m_State = False

    _m_FPS_MAX = 1/60

    _m_FPS = None

    _m_CurrentTime = 0.0
    _m_PrevTime = 0.0
    _m_AccTime = 0.0

    _m_Music=MusicConf.Music.songselect(1,1)


    def event_handler(self):
        event=get_events()

        for event in event:
            if event.type == SDL_QUIT:
                self._m_State=False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self._m_State=False


    def _create(self):
        open_canvas()
        self._m_State = True


    def _update(self):
        self.event_handler()
        pass


    def _draw(self):
        clear_canvas()
        gear = load_image('gear prot.png')
        gear.draw_now(400, 300)
        update_canvas()

    def _statebuild(self):
        pass


    def run(self):
        self._create()

        while self._m_State:
            self._m_CurrentTime = time.time()
            self._m_AccTime += self._m_CurrentTime - self._m_PrevTime
            self._m_PrevTime = self._m_CurrentTime
            if self._m_AccTime > self._m_FPS_MAX:
                self._m_FPS = 1 / self._m_AccTime
                self._update()
                self._draw()
                self._m_AccTime = 0

        self._exit()


    def _exit(self):
        self._m_State=False



P=Framework()
P.run()


