print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP19, board.GP4, board.GP6, board.GP8, board.GP10, board.GP13, board.GP15, board.GP17)
keyboard.row_pins = (board.GP0, board.GP11, board.GP3, board.GP14, board.GP5, board.GP16, board.GP7, board.GP18, board.GP9, board.GP12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    KC.DELETE, KC.BSPACE, KC.PSCREEN, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, 
     KC.NO, KC.NO, KC.NO, KC.N2, KC.NO, KC.NO, KC.NO, KC.PGUP,
     KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7,
     KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.BSLASH, KC.PGDN,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
     KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.SCOLON, KC.QUOTE, KC.ENTER,
     KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J,
     KC.K, KC.L, KC.KP_COMMA, KC.DOT, KC.SLASH, KC.UP, KC.DOWN, KC.RIGHT,
     KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M,
     KC.LGUI, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RSHIFT, 
]

if __name__ == '__main__':
    keyboard.go()

