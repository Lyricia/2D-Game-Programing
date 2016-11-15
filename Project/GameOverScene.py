from lylib import *

import MainFramework

class GameOverScene:

    _m_background = None
    _m_gameoverimage = None

    def __init__(self, pt_Framework):     # load music data
        self._m_background = load_image('Resources\\Image\\Background.png')
        self._m_gameoverimage = load_image('Resources\\Image\\gameover.png')
        self._m_stringfont = load_font('Resources\\Fonts\\String.ttf', 75)

        self._m_keys = []
        self.call_fw = pt_Framework
        self.fadeintimer = 0
        pass

    def handle_event(self):
        self._m_keys = SDL_GetKeyboardState(None)

        if self._m_keys[SDL_SCANCODE_RETURN]:
            self.call_fw._m_CurrentScene = 'MenuScene'
            self.call_fw.switchscene(self.call_fw._m_CurrentScene)

    def sceneupdate(self):  # update play scene -> time update
        self.handle_event()
        pass

    def scenedraw(self):
        self._m_background.draw(400, 380)
        self._m_gameoverimage.draw(400, 380, 800, 800)

        self._m_stringfont.draw(160, 100, str("Press Enter to back to menu"), (255,255,255))
