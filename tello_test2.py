from tello import Tello
import sys
from datetime import datetime
import time

commands_list = []#コマンド格納用リスト
command_list = []
start_time = str(datetime.now())

commandsList = []

isCreatedEmptyList = False

commandsCount = 0

i = 0

fileList = sys.argv[2:]#読み込むファイルのリスト
print(fileList)

while i <= len(fileList) -1:
    #fileListの要素数分回す
    with open(fileList[i], "r", encoding='utf-8') as f:
        getCommandList = [s.strip() for s in f.readlines()]
        commandsCount = len(getCommandList)
        n =0 #行数カウントをリセット

        #空のリスト作ってindexError防止(初回のみ実行)
        if isCreatedEmptyList == False:
            isCreatedEmptyList = True
            for num in range(commandsCount):
                commandsList.append([])

        #行の数だけ回してN番目のリストにi番目のファイルのN行目をINSERT
        while n <= commandsCount -1:
            commandsList[n].insert(n,getCommandList[n])
            n += 1
    i += 1

print(commandsList)
        
ip_file_name = sys.argv[1]

ip_f = open(ip_file_name, "r")
ips = ip_f.readlines()
ips = [ip.rstrip("\n") for ip in ips]#改行コード削除
ip_f.close

try:
    tello=Tello(ips)#txtファイルのipをリスト化して与える
    for commands in commandsList:
        print(commands)
        print(tello)
        tello.send_command(commands)

    log = tello.get_log()

    out = open('log/' + start_time + '.txt', 'w')
    for stat in log:
        stat.print_stats()
        str = stat.return_stats()
        out.write(str)
        
except KeyboardInterrupt:
	tello.send_command("command")
	tello.send_command("land")
	tello.send_command("emergency")


