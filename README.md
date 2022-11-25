# tello_test2
## Step1
command.txtを作る(書き換える):：
```
command
takeoff
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
```
$ Python3 tello_test2.py command.txt ip.txt
```
を実行する。
