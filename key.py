# -*- coding: utf-8 -*-
#Coded By Dark Slad3
#A Product Of Toxic Noobs

import os,sys,time
from time import sleep

a = "\033[32;1m"
b = "\033[0;32m"
c = "\033[34;1m"
d = "\033[36;1m"
e = "\033[31;1m"
f = "\033[0m"
f = "\033[37;1m"
g = "\033[35;1m"
h = "\033[3;1m"
i = "\033[33;1m"
j = "\033[0;33m"
k = "\033[30;1m"
l = "\x1b[0m"
m = "\x1b[31m"
n = "\x1b[1;32m"
o = "\x1b[33m"
p = "\x1b[34m"
q = "\x1b[35m"
r = "\x1b[36m"
gt = "\033[0;32m"

os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
    
os.system("clear")
time.sleep(1)
print ("\033[92m")
os.system("figlet Toxic Noobs")
print("\033[3;90m 			      Security is a Illusion\033[0;92m")
time.sleep(0.6)
psb("\n\n[!] Loading.....")
time.sleep(0.7)
psb("\n[!] Please Wait.....")
time.sleep(1)

os.system("clear")
time.sleep(0.5)
os.system("figlet TKey")
print("		A Product of Toxic Noobs")
time.sleep(0.7)
print
print("\033[1;94m────────────────────────────────────────────\x1b[1;94m")
print ("\033[1;92m▸ \033[92mAuthor   : M4lW4r3")
print ("\033[1;92m▸ \033[92mGithub   : https://github.com/toxicnoobs")
print("\033[1;94m────────────────────────────────────────────")
time.sleep(0.3)
                                
def toxickey():
		psb(' \033[1;33m\n[!] Process Started.....')
		sleep(1)
		os.mkdir('/data/data/com.termux/files/home/.termux')
		pass
		print(m+'   [√] First step Done...')
		sleep(1.2)
		key = "extra-keys = [['ESC','/','pwd','nano ','UP','clear','exit'] , ['TAB','CTRL','ALT ','LEFT','DOWN','RIGHT','-']] "
		kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
		kontol.write(key)
		kontol.close()
		print(m+ '   [√] Second step Done...')
		sleep(0.5)
		jalan(' \033[1;34m\n   [!] Refreshing Extra Key Settings......')
		os.system('termux-reload-settings')
		print(m+'   [√] Final step Done...')
		sleep(0.7)
		print(a+'   ')
		print(a+'   ')
		psb(' \033[1;36m  [*] Termux Extra Keys Successfully Installed by TKey...')
		sleep(0.8)
		sleep(1)
		os.system("clear")
		os.system("figlet Toxic Noobs")
		print("\033[3;90m 			      Security is a Illusion\033[0;37;40m")
		time.sleep(0.5)
		print
		print
		print



if __name__ == '__main__':
	toxickey()
