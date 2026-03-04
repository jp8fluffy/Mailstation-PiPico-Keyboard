# Mailstation-PiPico-Keyboard

Uses [Circuit Python](https://circuitpython.org/)  (built-in USB-HID modules) and [KMK](https://github.com/KMKfw/kmk_firmware) (Easy Keyboard Layout) with a [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) to 
convert the keyboard on the Cidco mailstation to a USB keyboard. 

<img width="665" height="318" alt="image" src="https://github.com/user-attachments/assets/465d21cc-89b3-42fb-a77b-fedfdf9e9e81" />

_Image courtesy of [Dr. Frankintosh](https://drfrancintosh.wordpress.com/cidco-mailstation/)_



## Mailstation Keyboard to PICO Pinout

![IMG_20260303_191644](https://github.com/user-attachments/assets/88ef083e-8115-4d15-9808-a617665cded1)

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

*Keyboard pin [mapping](https://github.com/kbembedded/mailstation/wiki/Keyboard-Information) 
was done based on the wonderful work of [Kris Bahnsen](https://github.com/kbembedded)*

## KMK Matrix
The rows and columns layout is a bit wierd. The following table was taken from [Kris Bahnsen's Repo on the Mailstation Keyboard](https://github.com/kbembedded/mailstation/wiki/Keyboard-Information)

|       | Col 7                | Col 6        | Col 5                  | Col 4 | Col 3 | Col 2   | Col 1 | Col 0         |
|-------|----------------------|--------------|------------------------|-------|-------|---------|-------|---------------|
| Row 0 | F5                   | F4           | F3                     | F2    | F1    | "Print" | "Back"| "Main Menu"   |
| Row 1 | "PgUp" ["Prev"]      | "Get E-Mail" | "Check Spelling"       | "Size"| @     |         |       |               |
| Row 2 | 7                    | 6            | 5                      | 4     | 3     | 2       | 1     | ` (Backtick)  |
| Row 3 | "PgDn" ["Next"]      | \            | "Delete" (Backspace)   | =     | -     | 0       | 9     | 8             |
| Row 4 | u                    | y            | t                      | r     | e     | w       | q     | "Tab"         |
| Row 5 | "Enter"              | '            | ;                      | ]     | [     | p       | o     | i             |
| Row 6 | j                    | h            | g                      | f     | d     | s       | a     | "Caps Lock"   |
| Row 7 | Right Arrow ["End"]  | Down Arrow   | Up Arrow               | /     | .     | ,       | l     | k             |
| Row 8 | m                    | n            | b                      | v     | c     | x       | z     | Left Shift    |
| Row 9 | Left Arrow ["Home"]  | Right Shift  |                        |       | Space |         |       | Fn / Function |
