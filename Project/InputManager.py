from sdl2 import *
from pico2d import *

def event_handler():  # not in progress, should separate to 'input manager'
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            self._m_State = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                self._m_State = False
            if event.key == SDLK_q:
                self._m_State = False

            if event.key == SDLK_s:
                if self._m_runMusic == False:
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
                    del (self._m_Music)
                    self._m_runMusic = False
                    self._m_CurrentScene = 'MenuScene'

            if event.key == SDLK_e and self._m_runMusic:
                # self._m_Music._m_CurrentNote.UpdateNote()
                self._m_Music._m_CurrentNote.notejudgechk()
                self._m_SpriteTimer.bSprite = True

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