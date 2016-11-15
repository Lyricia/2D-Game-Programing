from lylib import *

import MainFramework

class ResultScene:

    _m_background = None
    _m_resultimage = None

    def __init__(self, pt_Framework):     # load music data
        self._m_background = load_image('Resources\\Image\\Background.png')
        self._m_resultimage = load_image('Resources\\Image\\Result.png')
        self._m_numberfont = load_font('Resources\\Fonts\\Score.ttf', 40)
        self._m_resultfont = load_font('Resources\\Fonts\\Result.ttf', 75)
        self._m_stringfont = load_font('Resources\\Fonts\\String.ttf', 75)

        self._m_keys = []
        self.call_fw = pt_Framework

        self._m_Score = self.call_fw._m_player.score
        self._m_averageaccuracy = round(self.call_fw._m_player.avgacc, 2)
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
        self._m_resultimage.draw(400, 380, 800, 800)

        self._m_resultfont.draw(150,650,str("Result"))
        self._m_stringfont.draw(150, 450, str("Score :"))
        self._m_stringfont.draw(100, 350, str("Avg. Accuracy :"))

        self._m_numberfont.draw(450, 450, str(self._m_Score))
        self._m_numberfont.draw(450, 350, str(self._m_averageaccuracy)+'%')

        self._m_stringfont.draw(175, 100, str("Press Enter to back to menu"))

