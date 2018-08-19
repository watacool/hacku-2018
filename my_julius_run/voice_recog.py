# coding: utf-8
import os
import socket
from datetime import datetime
from time import sleep
from camera import shutter, dbx_upload

J_HOST = '127.0.0.1' # localhost
J_PORT = 10500   # julisu server's default port

TC_HOST = '127.0.0.1' #localhost
TC_PORT = 65535   # to control program's port

# define state
INIT = 'INIT' # waiting for 'ok julius'
CONTROL = 'CONTROL' # waiting for instruction of color

# define julius call
CALLJULIUS = ('ギース', 'オッケーギース', 'フローズンギース', 'オッケーフローズンギース', 'スノーギース')

# define word and color
RED = ('イチゴ', 'すいか', 'リンゴ')
BLUE = ('ブルーハワイ', )
GREEN = ('メロン', )
YELLOW = ('レモン', )
PURPLE = ('グレープ', 'ブドウ')
COLORFULL = ('レインボー', 'カラフル', '虹色')

SHUTTER = ('しゃしん', 'しゃしんとって', 'かんぱい')

DEBUG_MODE = 0

def parse_word(data_str):
    word = None
    data_str = data_str.split('\n')
    for str in data_str:
        if 'WHYPO' in str:
            start = str.find('"') + 1
            end = str.find('"', start)
            word = str[start:end]
            if '[s]' not in word and '[/s]' not in word:
                return word
    return None


def send_sig(sig):
    '''
    send to cotrol signal using UDP
    '''
    tc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tc_sock.sendto(sig.encode('utf-8'), (TC_HOST, TC_PORT))
    output = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    output += '\n## send signal: ' + sig
    print(output)
    if DEBUG_MODE == 1:
        with open("debug.txt", mode='a') as f:
            f.write(output)
    tc_sock.close()
    return 0

def main():
    '''
    reference
    https://qiita.com/nanako_ut/items/0b42cb956929a7ac739a
    '''
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((J_HOST, J_PORT))
    state = INIT
    pre_state = INIT
    while True:
        data = str(sock.recv(2048).decode('utf-8'))
        sleep(0.1)
        word = parse_word(data)

        # debug
        if DEBUG_MODE == 1:
            defugfile = "debug.txt"
            output = "data start\n" + data + "\ndata end\n"
            print(output)
            with open(defugfile, mode='a') as f:
                f.write(output)

        if word is None:
            print("Error: word is None")
            continue
        else:
            print("Word is {}".format(word))

        # switch state
        if word in CALLJULIUS:
            send_sig('')
            pre_state = state
            state = CONTROL
        elif state == CONTROL:
            if word in RED:
                send_sig('R')
            elif word in BLUE:
                send_sig('B')
            elif word in GREEN:
                send_sig('G')
            elif word in YELLOW:
                send_sig('GR')
            elif word in PURPLE:
                send_sig('RB')
            elif word in COLORFULL:
                send_sig('C')
            elif word in SHUTTER:
                send_sig('')
                send_sig('C')
                sleep(1.0)
                photo_dir = os.path.join(os.getcwd(), "camera", "photo")
                shutter.shutter(id='A', dir=photo_dir)
                dbx_upload.upload(dir=photo_dir)
                send_sig('')
                send_sig('C')
            else:
                pre_state = state
                output = "#### SKIP state is "+pre_state+" => " + state + " and receive " + word
                print(output)
                continue
            pre_state = state
            state = INIT
        else:
            pre_state = state
            state = INIT


        if word is not None: output = "## state is "+pre_state+" => "+state+" and receive "+word
        else: output = "## state is "+pre_state+" => "+state
        print(output)
        # debug
        if DEBUG_MODE == 1:
            with open(defugfile, mode='a') as f:
                f.write(output)

    sock.close()

if __name__ == "__main__":
    main()
