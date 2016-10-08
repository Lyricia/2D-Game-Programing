from lylib import *

import MusicConf

class PlayScene:

    _m_Musicdata = None
    _m_background_image = None
    _m_gear_image = None
    _m_note_image = None

    _m_Notedata = None

    def __init__(self,Musicdata):     # load music data
        self._m_Musicdata = Musicdata
        self._m_Notedata = Musicdata._m_CurrentNote._m_Notelist

        self._m_background_image = load_image('Resources\\Image\\Background.png')
        self._m_gear_image = load_image('Resources\\Image\\gear prot.png')
        self._m_note_image = load_image('Resources\\Image\\note p1.png')
        pass

    def sceneupdate(self):  # update play scene -> time update
        clear_canvas()

        #print('scene update func')
        self._m_background_image.draw(400, 380)
        self._m_gear_image.draw(400, 380)

        for idx in range(100):
            if self._m_Notedata[0][idx] != '0':
                self._m_note_image.draw(283, int(self._m_Notedata[0][idx]))

        update_canvas()
        pass