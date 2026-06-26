import numpy as np
import pyray as rl

# pychip8 timers
# by las-r

# timers class
class Timers:
    def __init__(self):
        self.delay = np.uint8(0)
        self.sound = np.uint8(0)
        self.playing = False
        
        rl.init_audio_device()
        
    def set_delay(self, val: int):
        self.delay = np.uint8(val)
        
    def set_sound(self, val: int):
        self.sound = np.uint8(val)

    def update(self):
        if self.delay > 0:
            self.delay -= 1
        if self.sound > 0:
            self.sound -= 1
            self.play_beep()
        else:
            self.stop_beep()

    def play_beep(self):
        if not self.playing:
            pass

    def stop_beep(self):
        pass
    
    def deinit(self):
        rl.close_audio_device()