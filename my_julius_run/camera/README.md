## RaspberryPiへのカメラモジュール設定手順

1. カメラの設定をONにする
```
$ sudo raspi-config
> Interface -> Camera
```

2. 再起動後にカメラが認識されているかの確認
```
$ vcgencmd get_camera
> supportedとdetectedが両方1であれば問題なし
```

3. raspistillコマンドを用いて写真撮影が行ることの確認
```
$ raspistill -q 100 -o ~/image_shell_local.jpg
```

## pythonへのカメラモジュール設定手順

* pipコマンドを用いてpicameraをインストールし，撮影が行えることの確認
```
$ pip install picamera
$ python
>>> import picamera
>>> with picamera.PiCamera() as camera:
>>> 	camera.capture('~/image_python_local.jpg')
>>> 	
>>> exit
```

## DropBoxのコマンド設定

* DropBox用コマンドを/usr/local/binへ登録し，アップロードが行えることの確認
```
$ cd
$ sudo git clone https://github.com/andreafabrizi/Dropbox-Uploader/
$ sudo chmod 755 Dropbox-Uploader/dropbox_uploader.shhttps://github.com/andreafabrizi/Dropbox-Uploader/
$ sudo cp dropbox_uploader.sh /usr/local/bin/
$ cd /usr/local/bin; sh dropbox_uploader.sh
> 保存先ディレクトリのトークンを入力
$ dropbox_uploader.sh upload ~/image_shell_local.jpg image_shell_cloud.jpg
$ dropbox_uploader.sh upload ~/image_python_local.jpg image_python_cloud.jpg
```
