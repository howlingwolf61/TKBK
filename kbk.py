import os
import time

#---renkler---
K='\033[1;91m'
Y='\033[1;92m'
S='\033[1;93m'
M='\033[1;94m'
P='\033[1;95m'
CG='\033[1;96m'
B='\033[1;97m'

os.system('clear')
os.system('sh kbk/banner.sh')
os.system('sleep 1')
os.system('cd $HOME && rm -rf kbk')

print ('')
malicious_kon = '/data/data/com.termux/files/home/Malicious'

if os.path.exists(malicious_kon):
        print (Y+"[✔]:[ Malicious Klasörü ]: "+CG+" Bulundu !\n")
        os.system('sleep 1')
        malicious_kb_kon = '/data/data/com.termux/files/usr/bin/Malicious'

        if os.path.exists(malicious_kb_kon):
                print (Y+"[✔]:[ Malicious Kolay Başlatıcı ]: "+CG+" Bulundu !\n")
                os.system('sleep 1')
        else:
                print (Y+"[x]:[ Malicious Kolay Başlatıcı ]: "+K+" Bulunamadı ! ")
                os.system("sleep 1 && echo '\033[1;93m'")
                malicious_kb_kur = input(S+'Malicious Kokay Başlatıcı Kurulsun mu? (y/n) > ')
                if malicious_kb_kur == 'y':
                        os.system("sleep 1 && echo")
                        print (S+"Malicious Kolay Başlatıcı Yükleniyor.....\n")
                        os.system('sleep 1')
                        os.system('cd $HOME')
                        os.system('git clone https://github.com/howlingwolf61/kbk')
                        os.system('mv kbk/Malicious ../usr/bin')
                        os.system('cd ../usr/bin')
                        os.system('chmod +x Malicious')
                        os.system('cd $Home')
                        os.system('rm -rf kbk')

else:
        print (Y+"[x]:[ Malicious Klasörü ]: "+K+" Bulunamadı ! ")
        os.system('sleep 1 && echo')
        malicious_kur = input(S+'Malicious Kurulsun mu? (y/n) > ')
        os.system('sleep 1 && echo')

        if malicious_kur == 'y':
                print (S+"Malicious Yükleniyor.....\n")
                apt = 'apt install'
                os.system(apt+' ruby python2 -y')
                os.system('gem install lolcat')
                os.system('cd $HOME')
                os.system('git clone https://github.com/Hider5/Malicious && echo')
                os.system('pip2 install -r $HOME/Malicious/requirements.txt')

os.system('sleep 1 && echo && echo')
malicious_kon = '/data/data/com.termux/files/home/A-Rat'

if os.path.exists(malicious_kon):
        print (Y+"[✔]:[ A-Rat Klasörü ]: "+CG+" Bulundu !\n")
        malicious_kb_kon = '/data/data/com.termux/files/usr/bin/A-Rat'

        os.system('sleep 1')
        if os.path.exists(malicious_kb_kon):
                print (Y+"[✔]:[ A-Rat Kolay Başlatıcı ]: "+CG+" Bulundu !\n")

                os.system('sleep 1')
        else:
                print (Y+"[x]:[ A-Rat Kolay Başlatıcı ]: "+K+" Bulunamadı ! ")
                print (S)
                malicious_kb_kur = input(S+'A-Rat Kokay Başlatıcı Kurulsun mu? (y/n) > ')
                if malicious_kb_kur == 'y':
                        os.system('sleep 1 && echo')
                        print (S+"A-Rat Kolay Başlatıcı Yükleniyor.....\n")
                        os.system('cd $HOME')
                        os.system('git clone https://github.com/howlingwolf61/Malicious-tr')
                        os.system('mv Malicious-tr/Malicious ../usr/bin')
                        os.system('cd ../usr/bin')
                        os.system('chmod +x Malicious')
                        os.system('cd $Home')
                        os.system('sleep 1 && echo')

else:
        print (Y+"[x]:[ A-Rat Klasörü ]: "+K+" Bulunamadı ! ")
        os.system('sleep 1 && echo')
        malicious_kur = input(S+'A-Rat Kurulsun mu? (y/n) > ')
        os.system('sleep 1 && echo')

        if malicious_kur == 'y':
                print (S+"A-Rat Yükleniyor.....\n")
                os.system('cd $HOME')
                os.system('git clone https://github.com/Hider5/Malicious && echo')