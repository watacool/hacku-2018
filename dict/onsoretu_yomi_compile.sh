#!/bin/bash

BASENAME=~/hacku-2018/dict/my_dict
iconv -f utf8 -t eucjp $BASENAME.yomi | yomi2voca.pl | iconv -f eucjp -t utf8 > $BASENAME.phone
