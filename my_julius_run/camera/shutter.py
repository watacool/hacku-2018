# coding: utf-8
import os
import argparse
import picamera
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, default='A')
    args = parser.parse_args()
    return args


def capture(title):
    '''
    reference
    https://iotdiyclub.net/raspberry-pi-camera-python-1/
    '''
    print("capture {}".format(title))
    with picamera.PiCamera() as camera:
        # flip upside down
        # camera.hflip = True
        # camera.vflip = True
        camera.capture(title)
    return 0

def shutter(id, dir=None):
    if dir is None: 
    	photo_dir = os.path.join(os.getcwd(), "photo")
    else:
    	photo_dir = dir
    title = "ID_{}_{}.jpg".format(id, datetime.now().strftime("%Y%m%d_%H%M%S"))
    if not os.path.exists(photo_dir):
        os.mkdir(photo_dir)
    title = os.path.join(photo_dir, title)
    capture(title)
    return 0


if __name__ == "__main__":
    args = get_args()
    shutter(args.id)
