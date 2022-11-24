# tello_test2
## Step1
command.txtを作る(書き換える):：
```
command
takeoff
land
```

## Step2
操作したいTelloの数だけTelloと接続し
```
$ Python3 tello_test wifi_setup.txt
```
を実行する

## Step3
```
$ arp -an
```

でTelloのmacアドレスを探してipを確認する

## Step４
ip.txtにStep3で調べたipを書き込む
```
Tello_ip0
Tello_ip1
・
・
・
```
## Step４
```
$ Python3 tello_test2 command.txt ip.txt
```
を実行する。
