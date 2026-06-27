from cpu import *
from display import *
from memory import *
from timers import *
import pyray as rl
import sys

# get rom bytes
romname = sys.argv[1]
with open(romname, "rb") as f:
    rom = f.read()
    
# init emulator
display = Display()
memory = Memory()
timers = Timers()
cpu = Processor(memory, display)

# main loop
while not rl.window_should_close():
    for _ in range(cpu.cpf):
        cpu.cycle()

# deinit
display.deinit()
timers.deinit()