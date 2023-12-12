import os
import requests
from bs4 import BeautifulSoup 

def sanggam1():
    try:
        print('-----------------------------------')
        print('|Author:Sanggam Sidabutar         |')
        print('|Github:github.com/sidabutar1337  |')
        print('|Facebook:facebook.com/zeussec1337|')
        print('-----------------------------------')
        url = input('input url: ')
        headers = {'User Agent':'Mozilla/5.0 (Linux; U; Android 7.1.2;9.2; Redmi 4A Build/N2G47H)3530 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.12893.0.5712.108 Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'}
        respons = requests.get(url,headers=headers)
        sidabutar = BeautifulSoup(respons.content,'html.parser')
        for dump in sidabutar.find_all('a'):
            print(dump.get('href'))
            with open('results.txt','w') as simpan:
                simpan.write(dump.get('href'))
                print('data berhasil di simpan!!')
        sanggam = input('apakah ingin menggunakan lagi?y/n ')
        if sanggam == 'y' or sanggam == 'Y':
            ulang = sanggam1()
            print(ulang)
        else:
            print('terima kasih telah menggunakan program saya')
            print('jika anda suka program ini berikan bintang')
            github = os.system('xdg-open https://github.com/sidabutar1337')
            print(github)
    except ConnectionError:
        print('koneksi kamu error')
        mulai1 = sanggam()
        print(mulai1)
name = input('siapa nama kamu? ')
gender = input('kamu cowo apa cewe? ')
if gender == 'cewe' or gender == 'Cewe':
    while True:
        tanya = input(f'halo {name} cantik menurut kamu aku ganteng gak? ')
        if tanya == 'iya' or tanya == 'ya' or tanya == 'Iya' or tanya == 'Ya':
            print(f'makasih {name} cantik')
            mulai = sanggam1()
            print(mulai)
            break
        else:
            print('Harus ganteng>//<')
elif gender == 'Cowo' or gender == 'cowo':
    print(f'halo bro {name} makasih udah mau pake tools gw mwheheh')
    mulai = sanggam1()
    print(mulai)
else:
    print('gender tidak ada')
    mulai = sanggam1()
    print(mulai)                                     
