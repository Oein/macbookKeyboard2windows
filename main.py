import pygame

# Define colors
KEY_OUTLINE = (50, 66, 74)
KEY_BG = (38, 50, 56)
DARK_GRAY = (169, 169, 169)

ofs = 20
KEY_TEXT_UNSELECTED = (63 + ofs, 84 + ofs, 94 + ofs)
KEY_TEXT_SELECTED = (141, 170, 184)

BG = (26, 34, 39)

screen_width = 800
screen_height = 400

# Define key layout
keys = [
    ["escape", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "delete"],
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "backspace"],
    "tab q w e r t y u i o p [ ] \\".split(),
    ["caps lock", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "return"],
    ["left shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "right shift"],
    ["fn", "left ctrl", "left alt", "left meta", "space", "right meta", "right alt", "left", "down", "right"],
]

keyAlias = {
    "left": ["home"],
    "right": ["end"],
    "down": ["page down"],
    "up": ["page up"],
}

# Special key width multipliers
keyWidthMapper = {
    "backspace": 1.5,
    "tab": 1.5,
    "caps lock": 1.82,
    "return": 1.82,
    "left shift": 2.35,
    "right shift": 2.35,
    "left meta": 1.23,
    "right meta": 1.23,
    "space": 5.4,
}

def get_key_width(key, base_width):
    """Calculate the width of each key, adjusting for special key width multipliers."""
    if key in keyWidthMapper:
        return base_width * keyWidthMapper[key]
    else:
        return base_width

keyMap = {
    '`' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '0' : 10,
    '-' : 11,
    '=' : 12,
    'q' : 13,
    'w' : 14,
    'e' : 15,
    'r' : 16,
    't' : 17,
    'y' : 18,
    'u' : 19,
    'i' : 20,
    'o' : 21,
    'p' : 22,
    '[' : 23,
    ']' : 24,
    '\\' : 25,
    'a' : 26,
    's' : 27,
    'd' : 28,
    'f' : 29,
    'g' : 30,
    'h' : 31,
    'j' : 32,
    'k' : 33,
    'l' : 34,
    ';' : 35,
    '\'' : 36,
    'z' : 37,
    'x' : 38,
    'c' : 39,
    'v' : 40,
    'b' : 41,
    'n' : 42,
    'm' : 43,
    ',' : 44,
    '.' : 45,
    '/' : 46,
    'left' : 47,
    'up' : 48,
    'down' : 49,
    'right' : 50,
    'tab' : 51,
    'left shift' : 52,
    'right shift' : 53,
    'backspace' : 54,
    'left ctrl' : 55,
    'left alt' : 56,
    'left meta' : 57,
    'right meta' : 58,
    'right alt' : 59,
    'right ctrl' : 60,
    'escape' : 61,
    'caps lock' : 62,
    'f1' : 63,
    'f2' : 64,
    'f3' : 65,
    'f4' : 66,
    'f5' : 67,
    'f6' : 68,
    'f7' : 69,
    'f8' : 70,
    'f9' : 71,
    'f10' : 72,
    'f11' : 73,
    'f12' : 74,
    'return' : 75,
    'delete' : 76,
    'page down' : 77,
    'page up' : 78,
    'space' : 79,
    'home': 80,
    'end': 81,

    'fn': 82,
}

kState = [0] * len(keyMap)

def draw_keyboard(screen, x, y, width, height):
    pygame.draw.rect(screen, BG, (0, 0, screen_width, screen_height), 0)
    # Set key dimensions based on the provided width and height
    row_height = height // len(keys)  # Height for each row
    base_key_width = width // max(len(row) for row in keys)  # Base width for each key

    fnEnabled = kState[keyMap["page down"]] or kState[keyMap["page up"]] or kState[keyMap["home"]] or kState[keyMap["end"]]
    
    # Iterate through each row
    for row_idx, row in enumerate(keys):
        total_row_width = 0
        key_widths = []
        
        # Calculate the total width for the current row
        for key in row:
            key_width = get_key_width(key, base_key_width)
            key_widths.append(key_width)
            total_row_width += key_width
        
        # Scale factor to adjust the widths so that the total row width matches the target width
        scale_factor = width / total_row_width
        
        # Draw each key in the row
        current_x = x  # Start X position for the row
        for key, key_width in zip(row, key_widths):
            adjusted_width = key_width * scale_factor  # Adjust width by scale factor

            kidx = keyMap[key]
            enabled = kState[kidx]

            if key == "fn":
                enabled = fnEnabled

            if key in keyAlias:
                for k in keyAlias[key]:
                    kidx = keyMap[k]
                    enabled = enabled or kState[kidx]

            yApd = 0
            yMul = 1

            if key == "left":
                yApd = 0.5
                yMul = 0.5
            elif key == "right":
                yApd = 0.5
                yMul = 0.5
            elif key == "down":
                yApd = 0.5
                yMul = 0.5
            
            # Draw the key (rectangle)
            keyColor = KEY_OUTLINE if enabled else KEY_BG
            pygame.draw.rect(screen, keyColor, (current_x, y + (row_idx + yApd) * row_height + (1 if yMul == 0.5 else 0), adjusted_width, row_height * yMul), 0)
            
            # Draw the key outline (border)
            borderColor = KEY_TEXT_SELECTED if enabled else KEY_OUTLINE
            pygame.draw.rect(screen, borderColor, (current_x, y + (row_idx + yApd) * row_height + (1 if yMul == 0.5 else 0), adjusted_width, row_height * yMul), 1)
            
            # Render the key label
            ftSize = 20
            if len(key) > 1:
                ftSize = 14
            if len(key) > 5:
                ftSize = 12

            txtColor = KEY_TEXT_SELECTED if enabled else KEY_TEXT_UNSELECTED

            ktext = key
            txtYMove = 0
            if key == "left":
                ktext = "←"
                ftSize = 12
                if kState[keyMap["home"]]:
                    ktext = "home"
            elif key == "right":
                ktext = "→"
                ftSize = 12
                if kState[keyMap["end"]]:
                    ktext = "end"
            elif key == "down":
                ktext = "↓"
                ftSize = 12
                if kState[keyMap["page down"]]:
                    ktext = "page down"
                    ftSize = 10
            elif "meta" in key:
                ktext = "⌘"
                ftSize = 24
                txtYMove = 3
            elif "alt" in key:
                ktext = "^"
                ftSize = 24
                txtYMove = 7
            elif "ctrl" in key:
                ktext = "ctrl"
            elif "shift" in key:
                ktext = "⇧"
                ftSize = 24
            
            font = pygame.font.SysFont('AppleSDGothicNeo', ftSize)
            text = font.render(ktext, True, txtColor)
            text_rect = text.get_rect(center=(current_x + adjusted_width // 2, y + (row_idx + yApd) * row_height + row_height * yMul // 2 + txtYMove))
            screen.blit(text, text_rect)

            if key == "down":
                # also draw the up key
                keyColor = KEY_OUTLINE if kState[keyMap["up"]] or kState[keyMap["page up"]] else KEY_BG
                pygame.draw.rect(screen, keyColor, (current_x, y + (row_idx) * row_height + (1 if yMul == 0.5 else 0), adjusted_width, row_height * 0.5), 0)
                borderColor = KEY_TEXT_SELECTED if kState[keyMap["up"]] or kState[keyMap["page up"]] else KEY_OUTLINE
                pygame.draw.rect(screen, borderColor, (current_x, y + (row_idx) * row_height + (1 if yMul == 0.5 else 0), adjusted_width, row_height * 0.5), 1)
                font = pygame.font.SysFont('AppleSDGothicNeo', 10 if kState[keyMap["page up"]] else 12)
                text = font.render("↑" if kState[keyMap["up"]] else "page up" if kState[keyMap["page up"]] else "↑", True, KEY_TEXT_SELECTED if kState[keyMap["up"]] or kState[keyMap["page up"]] else KEY_TEXT_UNSELECTED)
                text_rect = text.get_rect(center=(current_x + adjusted_width // 2, y + (row_idx) * row_height + row_height * 0.5 // 2 - 2))
                screen.blit(text, text_rect)
            
            # Move the X position for the next key
            current_x += adjusted_width


def printByteAsBin(byte):
    print(f'{byte:08b}')

def eightBoolsToByte(bools):
    byte = 0
    for i in range(8):
        byte += bools[i] << (7 - i)
    # printByteAsBin(byte.to_bytes(1, "big")[0])
    return byte.to_bytes(1, "big")

def num2_7bools(num):
    ret = [(num >> i) & 1 for i in range(6, -1, -1)]
    # print(ret)
    return ret

import sys
import glob
import serial

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

kHDK = [
    (8361, 96),
    (12610, 113),
    (12616, 119),
    (12599, 101),
    (12593, 114),
    (12613, 116),
    (12635, 121),
    (12629, 117),
    (12625, 105),
    (12624, 111),
    (12628, 112),

    (12609, 97),
    (12596, 115),
    (12615, 100),
    (12601, 102),
    (12622, 103),
    (12631, 104),
    (12627, 106),
    (12623, 107),
    (12643, 108),

    (12619, 122),
    (12620, 120),
    (12618, 99),
    (12621, 118),
    (12640, 98),
    (12636, 110),
    (12641, 109),
]

def keyHardMap(k):
    kn = pygame.key.name(k)
    print(k)
    if kn in keyMap:
        return kn
    
    for kH in kHDK:
        if kH[0] == k:
            return pygame.key.name(kH[1])
    
    return "UKN::" + str(k)

def main():
    print(serial_ports())
    ser = serial.Serial('/dev/cu.usbmodem13301', 115200)

    # Initialize pygame
    pygame.init()

    # Set up the pygame window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("MacBook Air 2020 Keyboard Layout")
    
    # Keyboard position and size
    x, y = 50, 65  # Starting position
    width, height = screen_width - 100, 270  # Size of the keyboard

    # Draw the keyboard
    draw_keyboard(screen, x, y, width, height)
    pygame.display.flip()
    
    # Main loop
    running = True
    while running:
        changed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ser.close()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                kn = keyHardMap(event.key)
                if not kn in keyMap:
                    print(f"Key {kn} not in keyMap {event.key}")
                    continue
                kidx = keyMap[kn]
                cmd = [1]
                cmd.extend(num2_7bools(kidx))
                kState[kidx] = 1
                changed = True
                ser.write(eightBoolsToByte(cmd))
            elif event.type == pygame.KEYUP:
                kn = keyHardMap(event.key)
                if not kn in keyMap:
                    print(f"Key {kn} not in keyMap")
                    continue
                kidx = keyMap[kn]
                cmd = [0]
                cmd.extend(num2_7bools(kidx))
                kState[kidx] = 0
                changed = True
                ser.write(eightBoolsToByte(cmd))
        
        if changed:
            draw_keyboard(screen, x, y, width, height)
            pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
