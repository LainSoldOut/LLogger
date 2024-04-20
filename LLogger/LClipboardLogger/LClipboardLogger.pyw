import pyperclip
import time

Ltime = time.strftime('%Y-%m-%d %H:%M:%S ')
Ltime2 = time.strftime('%Y-%m-%d %H.%M.%S ')
output_file = open(f'{Ltime2}Clipboard_log.txt', 'a')
PCC = ''

output_file.write(f'{Ltime}-------- ClipboardLogger has successfully started --------\n')

while True:
        CC = pyperclip.paste()
        if CC != PCC:
                output_file.write(f'{Ltime}'f'{CC}\n')
                output_file.flush()
                PCC = CC
        time.sleep(1)
