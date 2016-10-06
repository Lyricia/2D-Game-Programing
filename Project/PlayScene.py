from lylib import *

import MainFramework

class PlayScene:

    _m_Musicdata = None
    _m_background = None
    _m_gear = None
    _m_note = None

    def __init__(self,Musicdata):     # load music data
        self._m_Musicdata = Musicdata
        self._m_background = load_image('Resources\\Image\\Background.png')
        self._m_gear = load_image('Resources\\Image\\gear prot.png')
        self._m_note = load_image('Resources\\Image\\note p1.png')
        pass

    def _noteupdate(self):
        pass



    def sceneupdate(self):  # update play scene -> time update
        clear_canvas()

        print('scene update func')
        #print('%d' self._m_Musicdata)

        self._m_background.draw(400, 380)
        self._m_gear.draw(400, 380)
        self._m_note.draw(283,400)

        update_canvas()
        pass