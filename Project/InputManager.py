from pico2d import *
import sdl2


#def event(Musicdata):
#    keys = SDL_GetKeyboardState(None)
#
#    bKeyDown = False
#
#    if self.keys[SDL_SCANCODE_S]:
#        if self._m_runMusic == False:
#            self._m_runMusic = True
#            self._m_musicname = '120BPM'
#            self._m_CurrentScene = 'PlayScene'
#
#    if self._m_runMusic:
#        if self.keys[SDL_SCANCODE_E] and not self.bKeyDown:
#            self._m_Music._m_CurrentNote.notejudgechk(0)
#            self._m_SpriteTimer[0].bSprite = True
#        if self.keys[SDL_SCANCODE_R] and not self.bKeyDown:
#            self._m_Music._m_CurrentNote.notejudgechk(1)
#            self._m_SpriteTimer[1].bSprite = True
#        if self.keys[SDL_SCANCODE_U] and not self.bKeyDown:
#            self._m_Music._m_CurrentNote.notejudgechk(2)
#            self._m_SpriteTimer[2].bSprite = True
#        if self.keys[SDL_SCANCODE_I] and not self.bKeyDown:
#            self._m_Music._m_CurrentNote.notejudgechk(3)
#            self._m_SpriteTimer[3].bSprite = True
#
#    events = get_events()
#    for event in events:
#        if event.type == SDL_QUIT:
#            self._m_State = False
#        elif event.type == SDL_KEYDOWN:
#            if event.key == SDLK_ESCAPE:
#                self._m_State = False
#            if event.key == SDLK_q:
#                self._m_State = False
#