# coding: utf-8
import os
import argparse
import subprocess

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default=None)
    args = parser.parse_args()
    return args

def upload(dir=None):
    if dir is None:
        photo_dir = os.path.join(os.getcwd(), "photo")
    else:
        photo_dir = dir
    photo_list = os.listdir(photo_dir)
    for photo_local in photo_list:
        idx_start = photo_local.find('_') + 1
        idx_end = photo_local.find('_', idx_start)
        dbx_dir = "ID_" + photo_local[idx_start:idx_end]
        photo_cloud = os.path.join(dbx_dir, photo_local[idx_end+1:])
        photo_local = os.path.join(photo_dir, photo_local)
        upload_cmd = "/usr/local/bin/dropbox_uploader.sh upload {} {}".format(photo_local, photo_cloud)
        remove_cmd = "rm {}".format(photo_local)
        try:
            res = subprocess.check_call(upload_cmd, shell=True)
            res = subprocess.check_call(remove_cmd, shell=True)
        except:
            print("Error occured.\n\t{}".format(upload_cmd))
            continue

def main():
    args = get_args()
    upload(dir=args.dir)


if __name__ == "__main__":
    main()
