## HackU2018 の音声認識

### 環境
* OS：RASPBIAN STRETCH LITE
  * Version:June 2018
  * Release date:2018-06-27
  * Kernel version:4.14
* 音声認識エンジン：Julius4.4.2
* 言語：python3.6

### ファイル配置

* juliusと同じ階層に配置
* 例：/home/user/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| -- julius-4.4.2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| -- this repository  

### 実行方法

* my_julius_runフォルダに移動し，control_test_server.pyをバックグラウンドで実行後にrun.shを実行
```
$ cd ~/hacku-2018/my_julius_run
$ python control_test_server.py &
$ sh run.sh
```
* ※実行前にjuliusがバックグラウンドで起動していないことを確認する．起動していればプロセスをkillする
```
$ ps x
出力例：1194 pts/0    Sl     0:04 julius -C /home/user/julius-4.4.2/julius-kit/dictation-kit-v4.4/am-gmm.jconf
$ pkill -e julius
```

### 実行動画

* https://www.youtube.com/watch?v=MmwuqiqmXt4