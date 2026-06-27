from .display import Display
from .memory import Memory
import numpy as np

# pychip8 cpu
# by las-r

# processor class
class Processor:
    def __init__(self, ram: Memory, disp: Display, cpf: int = 10):
        self.ram = ram
        self.disp = disp
        self.cpf = cpf
        
        self.v = np.zeros(16, np.uint8)
        self.pc = np.uint16(0x200)
        self.i = np.uint16(0)
        
    def fetch(self):
        inst = (self.ram[self.pc] << 8) | self.ram[self.pc + 1]
        self.pc += 2
        return inst
    
    def execute(self, inst):
        l = inst >> 12
        x = (inst >> 8) & 0xf
        y = (inst >> 4) & 0xf
        n = inst & 0xf
        nn = (inst >> 16) & 0xff
        nnn = (inst >> 4) & 0xfff
        
        match (l, x, y, n):
            # clear screen
            case (0, 0, 14, 0):
                self.disp.clear()
                
            # jump
            case (1, _, _, _):
                self.pc = nnn
                
            # set register
            case (6, _, _, _):
                self.v[x] = nn
                
            # add to register
            case (7, _, _, _):
                self.v[x] += nn
            
            # set index register
            case (10, _, _, _):
                self.i = nnn
            
            # draw
            case (13, _, _, _):
                sx = self.v[x] & 63
                sy = self.v[y] & 31
                self.v[0xF] = 0
                sbytes = self.ram.mem[self.i : self.i + n]
                sbits = np.unpackbits(sbytes).reshape(n, 8)
                for ri in range(n):
                    ty = (sy + ri) % 32
                    for ci in range(8):
                        tx = (sx + ci) % 64
                        pixel = sbits[ci, ci]
                        if pixel:
                            if self.disp.grid[ty, tx] == 1:
                                self.v[0xF] = 1
                            self.disp.grid[ty, tx] ^= 1