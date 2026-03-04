print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

columns = [
       ]

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP17, # 0
    board.GP2, # 1
    board.GP4, # 2
    board.GP6, # 3
    board.GP8, # 4
    board.GP11, # 5
    board.GP13, # 6
    board.GP15 # 7
)
 
keyboard.row_pins = (
    board.GP0, # 0
    board.GP9, # 1
    board.GP1, # 2
    board.GP12, # 3
    board.GP3, # 4
    board.GP14, # 5
    board.GP5, # 6
    board.GP16, # 7
    board.GP7, # 8
    board.GP10 # 9
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
     KC.DELETE, KC.BSPACE, KC.PSCREEN, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, 
     KC.NO, KC.NO, KC.NO, KC.N2, KC.NO, KC.NO, KC.NO, KC.PGUP,
     KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7,
     KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.BSLASH, KC.PGDN,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
     KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.SCOLON, KC.QUOTE, KC.ENTER,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J,
     KC.K, KC.L, KC.COMMA, KC.DOT, KC.SLASH, KC.UP, KC.DOWN, KC.RIGHT,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M,
     KC.RCTRL, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RSHIFT, KC.LEFT
     ]
]

if __name__ == '__main__':
    keyboard.go()

