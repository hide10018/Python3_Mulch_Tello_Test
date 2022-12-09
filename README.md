# tello_test2
## Step1
操作したいドローンの数だけcommand.txtを作る(書き換える)
※行数を揃えないとダメです
:：
```
command
delay 10
takeoff
delay 10
land
```

## Step2
wifi_setup.txtを作る(書き換える):：
```
command
ap [SSID] [Password]
```

## Step3
操作したいTelloの数だけTelloと接続し
```
$ Python3 tello_test.py wifi_setup.txt
```
を実行する

## Step4
```
$ arp -an
```

でTelloのmacアドレスを探してipを確認する

## Step5
ip.txtにStep3で調べたipを書き込む
```
Tello_ip0
Tello_ip1
・
・
・
```
## Step6
接続しているドローンの数だけコマンドテキストを用意し、引数に追加する
```
$ Python3 tello_test2.py ip.txt command.txt command2.txt
```
を実行する。
