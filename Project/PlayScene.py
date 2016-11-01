from lylib import *

import SpriteConf
import MusicConf

class PlayScene:
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None
    _m_effect_sprite = None
    _m_scorefont = None


    def __init__(self, MusicData, Sprite, pt_Framework):     # load music data
        #self._m_Musicdata = Musicdata
        self._m_Musicdata = MusicData
        self._m_Notedata = MusicData._m_CurrentNote._m_Notelist
        self._m_sprite = Sprite
        self._m_keys = []
        self.call_fw = pt_Framework

        self.image_load()

    def handle_event(self):
        self._m_keys = SDL_GetKeyboardState(None)

        self.bKeyDown = False

        if self._m_keys[SDL_SCANCODE_E] :
            self._m_Musicdata._m_CurrentNote.notejudgechk(0)
            self._m_sprite[0].bSprite = True
        if self._m_keys[SDL_SCANCODE_R] :
            self._m_Musicdata._m_CurrentNote.notejudgechk(1)
            self._m_sprite[1].bSprite = True
        if self._m_keys[SDL_SCANCODE_U] :
            self._m_Musicdata._m_CurrentNote.notejudgechk(2)
            self._m_sprite[2].bSprite = True
        if self._m_keys[SDL_SCANCODE_I] :
            self._m_Musicdata._m_CurrentNote.notejudgechk(3)
            self._m_sprite[3].bSprite = True

        if self._m_keys[SDL_SCANCODE_1] and self._m_Musicdata._m_CurrentNote._m_speed != 1:
            self._m_Musicdata._m_CurrentNote._m_speed = 1
            self._m_Musicdata._m_CurrentNote._NotePosition()
        elif self._m_keys[SDL_SCANCODE_2] and self._m_Musicdata._m_CurrentNote._m_speed != 2:
            self._m_Musicdata._m_CurrentNote._m_speed = 2
            self._m_Musicdata._m_CurrentNote._NotePosition()
        elif self._m_keys[SDL_SCANCODE_3] and self._m_Musicdata._m_CurrentNote._m_speed != 3:
            self._m_Musicdata._m_CurrentNote._m_speed = 3
            self._m_Musicdata._m_CurrentNote._NotePosition()
        elif self._m_keys[SDL_SCANCODE_4] and self._m_Musicdata._m_CurrentNote._m_speed != 4:
            self._m_Musicdata._m_CurrentNote._m_speed = 4
            self._m_Musicdata._m_CurrentNote._NotePosition()
        elif self._m_keys[SDL_SCANCODE_5] and self._m_Musicdata._m_CurrentNote._m_speed != 5:
            self._m_Musicdata._m_CurrentNote._m_speed = 5
            self._m_Musicdata._m_CurrentNote._NotePosition()

        if self._m_keys[SDL_SCANCODE_M]:
            self.call_fw._m_Music.MusicStop()
            del(self.call_fw._m_Music)
            self.call_fw._m_runMusic = False
            self.call_fw.switchscene('MenuScene')

    def image_load(self):
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
        if not self._m_scorefont:
            self._m_scorefont = load_font('Resources\\Fonts\\Score.ttf',30)


    def sceneupdate(self):  # update play scene -> time update
        #print('scene update func')
        self.handle_event()

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

            if self._m_sprite[keyidx].bSprite:
                for frameidx in range(self._m_sprite[keyidx].SpriteFrame):
                    self._m_effect_sprite.clip_draw(self._m_sprite[keyidx].SpriteFrame * 192, 0, 192, 192,
                                                    283 + (70 * keyidx), 155,
                                                    120, 120)

        self._m_scorefont.draw(30, 100,str(self._m_Musicdata._m_CurrentNote._m_score) ,(255, 255, 255))

    def __del__(self):
        del (self._m_background_image)
        del (self._m_gear_image)
        del (self._m_note1_image)
        del (self._m_note2_image)
        del (self._m_effect_sprite)