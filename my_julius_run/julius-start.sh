#!/bin/bash

MY_DICT=~/hacku-2018/dict/my_dict
julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.4/am-gmm.jconf -gram $MY_DICT -module > /dev/null &
echo $!
sleep 1
