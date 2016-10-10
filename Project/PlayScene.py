from lylib import *

import MusicConf

class PlayScene:

    _m_Musicdata = None
    _m_background_image = None
    _m_gear_image = None
    _m_note1_image = None
    _m_note2_image = None

    _m_line = None

    _m_Notedata = None

    def __init__(self,Musicdata):     # load music data
        self._m_Musicdata = Musicdata
        self._m_Notedata = Musicdata._m_CurrentNote._m_Notelist

        self._m_background_image = load_image('Resources\\Image\\Background.png')
        self._m_gear_image = load_image('Resources\\Image\\gear prot.png')
        self._m_note1_image = load_image('Resources\\Image\\note p1.png')
        self._m_note2_image = load_image('Resources\\Image\\note p2.png')
        self._m_line = load_image('Resources\\Image\\line.png')

        self.liney = 760
        pass

    def sceneupdate(self):  # update play scene -> time update
        clear_canvas()

        #print('scene update func')
        self._m_background_image.draw(400, 380)
        self._m_gear_image.draw(400, 380)

        for keyidx in range(4):
            for idx in range(len(self._m_Notedata[keyidx])):
                if self._m_Notedata[keyidx][idx] != '0' and int(self._m_Notedata[keyidx][idx]) > 127:
                    if keyidx % 2 == 0:
                        self._m_note1_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))
                    elif keyidx % 2 == 1:
                        self._m_note2_image.draw(283 + 69 * keyidx, int(self._m_Notedata[keyidx][idx]))

        self.liney += 12 * 2/3
        if self.liney > 640:
            self.liney = 0
        #self.liney - (self._m_Musicdata._m_CurrentSongBPM / 60 * self._m_Musicdata._m_CurrentNote._m_speed)
        self._m_line.draw(400, 760 - self.liney)


        update_canvas()
        pass