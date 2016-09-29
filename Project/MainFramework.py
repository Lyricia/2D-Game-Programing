from lylib import *

import MusicConf

class Framework:

    _m_State = False

    _m_FPS_MAX = 1/60

    _m_FPS = None

    _m_CurrentTime = 0.0
    _m_PrevTime = 0.0
    _m_AccTime = 0.0

    _m_Music = None


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


    def _create(self):
        open_canvas(800,760)


    def _update(self):
        self.event_handler()
        if self._m_Music == None:
            self._m_Music = MusicConf.Music('evans')
            if self._m_Music:
                Mbox("end", "end", 0)
        pass

    def _draw(self):
        clear_canvas()
        background = load_image('Resources\\Image\\Background.png')
        gear = load_image('Resources\\Image\\gear prot.png')
        background.draw_now(400, 380)
        gear.draw_now(400, 380)

        update_canvas()

    def _statebuild(self):
        pass


    def run(self):
        self._create()
        self._m_State=True
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