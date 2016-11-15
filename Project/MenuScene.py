from lylib import *

import MainFramework

class MenuScene:

    _m_background = None
    _m_menu = None

    def __init__(self, pt_Framework):     # load music data
        self._m_background = load_image('Resources\\Image\\Background.png')
        self._m_menu = load_image('Resources\\Image\\menu.png')
        self._m_titlefont = load_font('Resources\\Fonts\\Title.ttf', 100)
        self._m_stringfont = load_font('Resources\\Fonts\\String1.ttf', 50)

        self._m_keys = []
        self.call_fw = pt_Framework
        pass

    def handle_event(self):
        self._m_keys = SDL_GetKeyboardState(None)

        if self._m_keys[SDL_SCANCODE_S]:
            self.call_fw._m_musicname = '120BPM'
            self.call_fw._m_CurrentScene = 'PlayScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)
        if self._m_keys[SDL_SCANCODE_D]:
            self.call_fw._m_musicname = 'Evans'
            self.call_fw._m_CurrentScene = 'PlayScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)
        if self._m_keys[SDL_SCANCODE_A]:
            self.call_fw._m_musicname = '180BPM'
            self.call_fw._m_CurrentScene = 'PlayScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)

        if self._m_keys[SDL_SCANCODE_G]:
            self.call_fw._m_CurrentScene = 'GameOverScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)

        if self._m_keys[SDL_SCANCODE_R]:
            self.call_fw._m_CurrentScene = 'ResultScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)

    def sceneupdate(self ):  # update play scene -> time update

        #print('menu update func')
        self.handle_event()
        pass

    def scenedraw(self):
        self._m_background.draw(400, 380)
        self._m_menu.draw(400, 380,1000, 750)
        self._m_titlefont.draw(85, 500, str("Drop Da BEAT"), (255,150,0))
        self._m_stringfont.draw(175,100, str("Press Enter to Start"), (255,255,255))