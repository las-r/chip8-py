import numpy as np
import pyray as rl

# pychip8 display
# by las-r

# display class
class Display:
    def __init__(self, scale: int = 12, title: str = "pychip8", fg: int = 0xFFFFFFFF, bg: int = 0x000000FF):
        self.cols = 64
        self.rows = 32
        self.scale = scale
        self.grid = np.zeros((self.rows, self.cols), dtype=np.uint8)
        self.on = rl.get_color(fg)
        self.off = rl.get_color(bg)

        rl.init_window(self.cols * self.scale, self.rows * self.scale, title)
        rl.set_target_fps(60)

    def clear(self):
        self.grid.fill(0)

    def render(self):
        rl.begin_drawing()
        rl.clear_background(self.off)
        
        for y in range(self.rows):
            for x in range(self.cols):
                if self.grid[y, x] == 1:
                    rl.draw_rectangle(
                        x * self.scale,
                        y * self.scale,
                        self.scale,
                        self.scale,
                        self.on
                    )
                    
        rl.end_drawing()

    def deinit(self):
        rl.close_window()