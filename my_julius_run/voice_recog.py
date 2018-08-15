# coding: utf-8
import socket
from datetime import datetime

J_HOST = '127.0.0.1' # localhost
J_PORT = 10500   # julisu server's default port

TC_HOST = '127.0.0.1' #localhost
TC_PORT = 65535   # to control program's port

# define state
INIT = 'INIT' # waiting for 'ok julius'
CONTROL = 'CONTROL' # waiting for instruction of color

# define julius call
CALLJULIUS = ('ジュリアス', 'オッケージュリアス', 'ジュリウス', 'オッケージュリウス')

# define word and color
RED = ('イチゴ', 'すいか', 'リンゴ')
BLUE = ('ブルーハワイ', )
GREEN = ('メロン', )
YELLOW = ('レモン', )
PURPLE = ('グレープ', 'ブドウ')
COLORFULL = ('レインボー', 'カラフル', '虹色')

DEBUG_MODE = 0

def parse_word(data_str):
    word = None
    state = 1
    keys = ["[/s]"]
    for key in keys:
        if key not in data_str:
            state = 0
    if state == 1:
        start = data_str.find('"') + 1
        end = data_str.find('"', start)
        if start == -1 or end == -1:
            word = None
        else:
            word = data_str[start:end]
    return word

def send_sig(sig):
    '''
    send to cotrol signal using UDP
    '''
    tc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tc_sock.sendto(sig.encode('utf-8'), (TC_HOST, TC_PORT))
    if DEBUG_MODE == 1:
        output = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        output += '## send signal: '+sig
        print(output)
        with open("debug.txt", mode='a') as f:
            f.write(output)
    return 0

def main():
    '''
    reference
    https://qiita.com/nanako_ut/items/0b42cb956929a7ac739a
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((J_HOST, J_PORT))
    state = INIT
    while True:
        data = str(sock.recv(2048).decode('utf-8'))
        word = parse_word(data)

        # debug
        if DEBUG_MODE == 1:
            defugfile = "debug.txt"
            output = "data start\n" + data + "\ndata end\n"
            if word is not None: output += "word start\n" + word + "\nword end\n"
            print(output)
            with open(defugfile, mode='a') as f:
                f.write(output)

        if word is None:
            print("Error: word is None")
            continue

        # switch state
        if word in CALLJULIUS:
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
            state = INIT
        else:
            state = INIT

        # debug
        if DEBUG_MODE == 1:
            if word is not None: output = "## state is "+state+" and receive "+word+"\n"
            else: output = "## state is "+state+"\n"
            print(output)
            with open(defugfile, mode='a') as f:
                f.write(output)

    sock.close()

if __name__ == "__main__":
    main()
