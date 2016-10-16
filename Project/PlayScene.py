from lylib import *

import SpriteConf

class PlayScene:
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None
    _m_effect_sprite = None
    _m_sprite = None
    def __init__(self,Musicdata):     # load music data
        self._m_Musicdata = Musicdata
        self._m_Notedata = Musicdata._m_CurrentNote._m_Notelist
        if not self._m_background_image:
            self._m_background_image = load_image('Resources\\Image\\Background.png')
        if not self._m_gear_image:
            self._m_gear_image = load_image('Resources\\Image\\gear prot.png')
        if not self._m_note1_image:
            self._m_note1_image = load_image('Resources\\Image\\note p1.png')
        if not self._m_note2_image:
            self._m_note2_image = load_image('Resources\\Image\\note p2.png')
        if not self._m_effect_sprite:
            self._m_effect_sprite = load_image('Resources\\Image\\effect.png')
        pass

    def sceneupdate(self):  # update play scene -> time update
        clear_canvas()
        #print('scene update func')
        self._m_background_image.draw(400, 380)
        self._m_gear_image.draw(400, 380)

        for keyidx in range(4):
            for idx in range(len(self._m_Notedata[keyidx])):
                if self._m_Notedata[keyidx][idx] != '0':
                    if int(self._m_Notedata[keyidx][idx]) > 0 and int(self._m_Notedata[keyidx][idx]) < 760:
                        if keyidx % 2 == 0:
                            self._m_note1_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))
                        elif keyidx % 2 == 1:
                            self._m_note2_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))


        update_canvas()
        pass

    def __del__(self):
        del (self._m_background_image)
        del (self._m_gear_image)
        del (self._m_note1_image)
        del (self._m_note2_image)
        del (self._m_effect_sprite)