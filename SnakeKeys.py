"""
    @author Grace Keane

    SnakeKeys - Class that defines keyboard controls.
"""

# Necessary Imports
# Provides C compatible data types, and allows calling functions
import ctypes

SendInput = ctypes.windll.user32.SendInput

# Snake up
up = 0x26
# Snake down
down = 0x28
# Snake left
left = 0x25
# Snake right
right = 0x27

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class keyboard_i(ctypes.Structure):
    _fields_ = [("KI1", ctypes.c_ushort),
                ("KI2", ctypes.c_ushort),
                ("Flags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("ExtraInfo", PUL)]

class hardware_i(ctypes.Structure):
    _fields_ = [("Msg", ctypes.c_ulong),
                ("upParamL", ctypes.c_short),
                ("upParamH", ctypes.c_ushort)]

class input_1(ctypes.Union):
    _fields_ = [("kbi", keyboard_i),
                ("hwi", hardware_i)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("input", input_1)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    input_ = input_1()
    input_.kbi = keyboard_i( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), input_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    input_ = input_1()
    input_.kbi = keyboard_i( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), input_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Calling and setting functions
if __name__ == '__main__':
    PressKey(0x26)
    ReleaseKey(0x26)
