from lylib import *

import MainFramework

class MenuScene:

    _m_background = None
    _m_menu = None

    def __init__(self):     # load music data
        self._m_background = load_image('Resources\\Image\\Background.png')
        self._m_menu = load_image('Resources\\Image\\menu.png')
        pass

    def sceneupdate(self):  # update play scene -> time update

        #print('menu update func')

        self._m_background.draw(400, 380)
        self._m_menu.draw(400,380)

        pass