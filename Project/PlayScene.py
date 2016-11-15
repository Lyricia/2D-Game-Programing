from lylib import *

import SpriteConf
import MusicConf

class PlayScene:
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None
    _m_effectsprite_image = None
    _m_keysprite_image = None
    _m_scorefont = None
    _m_isPause = False


    def __init__(self, pt_Framework, Musictitle):     # load music data
        self._m_Musicdata = MusicConf.Music(Musictitle)
        self._m_Notedata = self._m_Musicdata._m_CurrentNote._m_Notelist
        self._m_keys = []
        self.call_fw = pt_Framework

        self._m_keysprite = list()
        self._m_effectsprite = list()
        for idx in range(self._m_Musicdata._m_CurrentNote._m_keynum):
            self._m_keysprite.append(SpriteConf.Sprite('keysprite'))
            self._m_effectsprite.append(SpriteConf.Sprite('effect'))

        self.call_fw._m_NoteTimer = self._m_Musicdata._m_CurrentNote.NoteTimer
        self.call_fw._m_KeySpriteTimer = self._m_keysprite
        self.call_fw._m_EffectSpriteTimer = self._m_effectsprite

        self.image_load()

    def handle_event(self):
        self._m_keys = SDL_GetKeyboardState(None)

        if self._m_keys[SDL_SCANCODE_E] :
            if self._m_Musicdata._m_CurrentNote.notejudgechk(0):
                self._m_effectsprite[0].bSprite = True
                self._m_effectsprite[0].SpriteFrame = 0
            self._m_keysprite[0].bSprite = True
            self._m_keysprite[0].framelock = True
        if self._m_keys[SDL_SCANCODE_R] :
            if self._m_Musicdata._m_CurrentNote.notejudgechk(1):
                self._m_effectsprite[1].bSprite = True
                self._m_effectsprite[1].SpriteFrame = 0
            self._m_keysprite[1].bSprite = True
            self._m_keysprite[1].framelock = True
        if self._m_keys[SDL_SCANCODE_U] :
            if self._m_Musicdata._m_CurrentNote.notejudgechk(2):
                self._m_effectsprite[2].bSprite = True
                self._m_effectsprite[2].SpriteFrame = 0
            self._m_keysprite[2].bSprite = True
            self._m_keysprite[2].framelock = True
        if self._m_keys[SDL_SCANCODE_I] :
            if self._m_Musicdata._m_CurrentNote.notejudgechk(3):
                self._m_effectsprite[3].bSprite = True
                self._m_effectsprite[3].SpriteFrame = 0
            self._m_keysprite[3].bSprite = True
            self._m_keysprite[3].framelock = True

        if not self._m_keys[SDL_SCANCODE_E]:
            self._m_keysprite[0].framelock = False
        if not self._m_keys[SDL_SCANCODE_R]:
            self._m_keysprite[1].framelock = False
        if not self._m_keys[SDL_SCANCODE_U]:
            self._m_keysprite[2].framelock = False
        if not self._m_keys[SDL_SCANCODE_I] :
            self._m_keysprite[3].framelock = False


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

        if self._m_keys[SDL_SCANCODE_P]:
            self._m_isPause = True

        if self._m_keys[SDL_SCANCODE_M]:
            self._m_Musicdata.MusicStop()
            del(self._m_Musicdata)
            self._m_Musicdata = None
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
        if not self._m_effectsprite_image:
            self._m_effectsprite_image = load_image('Resources\\Image\\effect.png')
            self._m_effectsprite_image.opacify(0.1)
        if not self._m_keysprite_image:
            self._m_keysprite_image = load_image('Resources\\Image\\KeySprite.png')
            self._m_keysprite_image.opacify(0.1)
        if not self._m_scorefont:
            self._m_scorefont = load_font('Resources\\Fonts\\Score.ttf',15)


    def sceneupdate(self):  # update play scene -> time update

        self.handle_event()

        if self._m_Musicdata is not None:
            for keyidx in range(self._m_Musicdata._m_CurrentNote._m_keynum):
                if self._m_keysprite[keyidx].framelock and self._m_keysprite[keyidx].SpriteFrame is 5:
                    self._m_keysprite[keyidx].SpriteFrame -= 1

            if self._m_Musicdata.MusicFinished():
                self._m_Musicdata.MusicStop()
                del (self._m_Musicdata)
                self._m_Musicdata = None
                self.call_fw._m_runMusic = False
                self.call_fw.switchscene('MenuScene')

    def scenedraw(self):
        self._m_background_image.draw(400, 380)
        self._m_gear_image.draw(400, 380)
        self._m_scorefont.draw(30, 100, str(self._m_Musicdata._m_CurrentNote._m_score), (255, 255, 255))
        self._m_scorefont.draw(30, 150, str(self._m_Musicdata._m_CurrentNote._m_accuracy) + '%', (255, 255, 255))

        draw_rectangle(200,0,450,142)

        #self._m_scorefont.draw(30, 200, str(self._m_Musicdata._m_CurrentNote._m_CurrentNoteIdx),(255,255,255))

        for keyidx in range(4):
            if self._m_keysprite[keyidx].bSprite:
                for frameidx in range(self._m_keysprite[keyidx].SpriteFrame):
                    self._m_keysprite_image.clip_draw(self._m_keysprite[keyidx].SpriteFrame * 66, 0, 66,  600,
                                                    283 + (69  * keyidx), 455,
                                                    69, 600)

            for idx in range(len(self._m_Notedata[keyidx])):
                if self._m_Notedata[keyidx][idx] != '0':
                    if int(self._m_Notedata[keyidx][idx]) > 0 and int(self._m_Notedata[keyidx][idx]) < 760:
                        self._m_scorefont.draw(200, int(self._m_Notedata[keyidx][idx]), str(idx),(255,255,255))
                        if keyidx % 2 == 0:
                            self._m_note1_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))
                        elif keyidx % 2 == 1:
                            self._m_note2_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))

            if self._m_effectsprite[keyidx].bSprite:
                for frameidx in range(self._m_effectsprite[keyidx].SpriteFrame):
                    self._m_effectsprite_image.clip_draw(self._m_effectsprite[keyidx].SpriteFrame * 192, 0, 192, 192,
                                                         283 + (69 * keyidx), 155, 120, 120)

    def spritereturn(self):
        return self._m_keysprite

    def __del__(self):
        del (self._m_background_image)
        del (self._m_gear_image)
        del (self._m_note1_image)
        del (self._m_note2_image)
        del (self._m_effectsprite_image)