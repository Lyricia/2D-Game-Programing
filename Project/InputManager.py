from pico2d import *
import sdl2

class InputManager:

    def __init__(self):
        self.keys = None

    def event(self):  # not in progress, should separate to 'input manager'
        self.keys = sdl2.SDL_GetKeyboardState(None)
        if self.keys[SDL_SCANCODE_LEFT]:
            print('left')
        else: return
