from lylib import *

import SpriteConf

class PlayScene:
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None
    _m_effect_sprite = None
    def __init__(self, Musicdata, Sprite):     # load music data
        self._m_Musicdata = Musicdata
        self._m_Notedata = Musicdata._m_CurrentNote._m_Notelist
        self._m_sprite = Sprite

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
            self._m_effect_sprite.opacify(0.1)
        pass

    def sceneupdate(self):  # update play scene -> time update
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


        for keyidx in range(self._m_Musicdata._m_CurrentNote._m_keynum):
            if self._m_sprite[keyidx].bSprite:
                for frameidx in range(self._m_sprite[keyidx].SpriteFrame):
                    self._m_effect_sprite.clip_draw(self._m_sprite[keyidx].SpriteFrame * 192, 0, 192, 192, 283, 159)


        if self._m_sprite[0].bSprite:
            for frameidx in range(self._m_sprite[0].SpriteFrame):
                self._m_effect_sprite.clip_draw(self._m_sprite[0].SpriteFrame*192, 0, 192,192,283,159)
                print(self._m_sprite[0].SpriteFrame)
        if self._m_sprite[1].bSprite:
            for frameidx in range(self._m_sprite[1].SpriteFrame):
                self._m_effect_sprite.clip_draw(self._m_sprite[1].SpriteFrame*192, 0, 192,192,400,159)


        pass

    def __del__(self):
        del (self._m_background_image)
        del (self._m_gear_image)
        del (self._m_note1_image)
        del (self._m_note2_image)
        del (self._m_effect_sprite)