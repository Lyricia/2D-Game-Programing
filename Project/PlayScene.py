from lylib import *

import SpriteConf
import MusicConf

class PlayScene:
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None
    _m_effect_sprite = None


    def __init__(self, Musicdata, Sprite):     # load music data
        #self._m_Musicdata = Musicdata
        self._m_Musicdata = MusicConf.Music('Evans')
        self._m_Notedata = Musicdata._m_CurrentNote._m_Notelist
        self._m_sprite = Sprite
        self._m_keys = []

        self.image_load()

    def handle_event(self):
        self.keys = SDL_GetKeyboardState(None)

        self.bKeyDown = False

        if self.keys[SDL_SCANCODE_S]:
            if self._m_runMusic == False:
                self._m_runMusic = True
                self._m_musicname = '120BPM'
                self._m_CurrentScene = 'PlayScene'

        if self._m_runMusic:
            if self.keys[SDL_SCANCODE_E] and not self.bKeyDown:
                self._m_MusicData._m_CurrentNote.notejudgechk(0)
                self._m_SpriteTimer[0].bSprite = True
            if self.keys[SDL_SCANCODE_R] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(1)
                self._m_SpriteTimer[1].bSprite = True
            if self.keys[SDL_SCANCODE_U] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(2)
                self._m_SpriteTimer[2].bSprite = True
            if self.keys[SDL_SCANCODE_I] and not self.bKeyDown:
                self._m_Music._m_CurrentNote.notejudgechk(3)
                self._m_SpriteTimer[3].bSprite = True

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self._m_State = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self._m_State = False
                if event.key == SDLK_q:
                    self._m_State = False

                if self._m_runMusic and self._m_Music:
                    if event.key == SDLK_1 and self._m_Music._m_CurrentNote._m_speed != 1:
                        self._m_Music._m_CurrentNote._m_speed = 1
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_2 and self._m_Music._m_CurrentNote._m_speed != 2:
                        self._m_Music._m_CurrentNote._m_speed = 2
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_3 and self._m_Music._m_CurrentNote._m_speed != 3:
                        self._m_Music._m_CurrentNote._m_speed = 3
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_4 and self._m_Music._m_CurrentNote._m_speed != 4:
                        self._m_Music._m_CurrentNote._m_speed = 4
                        self._m_Music._m_CurrentNote._NotePosition()
                    elif event.key == SDLK_5 and self._m_Music._m_CurrentNote._m_speed != 5:
                        self._m_Music._m_CurrentNote._m_speed = 5
                        self._m_Music._m_CurrentNote._NotePosition()
        pass

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

            if self._m_sprite[keyidx].bSprite:
                for frameidx in range(self._m_sprite[keyidx].SpriteFrame):
                    self._m_effect_sprite.clip_draw(self._m_sprite[keyidx].SpriteFrame * 192, 0, 192, 192,
                                                    283 + (70 * keyidx), 155,
                                                    120, 120)

    def __del__(self):
        del (self._m_background_image)
        del (self._m_gear_image)
        del (self._m_note1_image)
        del (self._m_note2_image)
        del (self._m_effect_sprite)