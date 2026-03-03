# Mailstation-PiPico-Keyboard
Uses [Circuit Python's](https://circuitpython.org/) built-in USB-HID modules along with a [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) to convert the keyboard on the Cidco mailstation to a USB keyboard.

## Mailstation Keyboard to PICO Pinout
| **Signal** | **Keyboard Pins** | **Pico Pins** |
|------------|-------------------|---------------|
| Col 0      | 18                | GP17          |
| Col 1      | 3                 | GP2           |
| Col 2      | 5                 | GP4           |
| Col 3      | 7                 | GP6           |
| Col 4      | 9                 | GP8           |
| Col 5      | 12                | GP11          |
| Col 6      | 14                | GP13          |
| Col 7      | 16                | GP15          |
| Row 0      | 1                 | GP0           |
| Row 1      | 10                | GP9           |
| Row 2      | 2                 | GP1           |
| Row 3      | 13                | GP12          |
| Row 4      | 4                 | GP3           |
| Row 5      | 15                | GP14          |
| Row 6      | 6                 | GP5           |
| Row 7      | 17                | GP16          |
| Row 8      | 8                 | GP7           |
| Row 9      | 11                | GP10          |

