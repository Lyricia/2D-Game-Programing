from pico2d import *
import time
import Logo_Scene
import Title_Scene
import Play_Scene
import GameOver_Scene
import Ranking_Scene


class Framework:
    _m_bRun = False

    MAX_FPS = 1 / 60  # 1 / FPS
    _m_FPS = None
    _m_PrevTime = None
    _m_CurrentTime = None
    _m_AccumulatedTime = None

    _m_Logo = Logo_Scene.LogoScene()
    _m_Title = Title_Scene.TitleScene()
    _m_Play = Play_Scene.PlayScene()
    _m_Gameover = GameOver_Scene.GameoverScene()
    _m_Ranking = Ranking_Scene.RankingScene()

    _m_CurrentScene = None
    _m_SoundManager = None

    def _create(self):
        open_canvas()
        self._build_scene()
        self._m_bRun = True

    def _build_scene(self):
        self._m_Logo.build_object(self)
        self._m_Title.build_object(self)
        self._m_Play.build_object(self)
        self._m_Gameover.build_object(self)
        self._m_Ranking.build_object(self)

        self._m_CurrentScene = self._m_Logo

    def _update(self, TimeElapsed):
        self._m_CurrentScene.update(TimeElapsed)

    def _draw(self):
        clear_canvas()
        self._m_CurrentScene.draw()
        update_canvas()

    def _release_scene(self):
        self._m_Logo.release()
        self._m_Title.release()
        self._m_Play.release()
        self._m_Gameover.release()
        self._m_Ranking.release()

    def _exit(self):
        self._release_scene()
        close_canvas()

    def change_scene(self, tag):
        pass

    def run(self):
        self._create()

        while self._m_bRun:
            self._m_CurrentTime = time.time()
            self._m_AccumulatedTime += self._m_CurrentTime - self._m_PrevTime
            self._m_PrevTime = self._m_CurrentTime
            if self._m_AccumulatedTime > self.MAX_FPS:
                self._m_FPS = 1 / self._m_AccumulatedTime  # FPS = 1 / ( 1 / 60 )
                self._update(self._m_AccumulatedTime)
                self._draw()
                self._m_AccumulatedTime = 0

        self._exit()

    def quit(self):
        self._m_bRun = False
        self._m_CurrentScene = None
        self._m_SoundManager = None


