#!/bin/bash

export ALSADEV="plughw:1,0"
/usr/local/bin/julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.4/am-gmm.jconf -gram ~/hacku-2018/dict/my_dict -module > /dev/null &
sleep 2
cd ~/hacku-2018/my_julius_run; /usr/bin/nohup /usr/bin/python voice_recog.py &
