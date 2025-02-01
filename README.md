# FTP-BruteR

**FTP-BruteR**: Güçlü bir FTP kaba kuvvet aracı, kullanıcı adı ve şifre listesi ile FTP sunucusuna saldırı yapmayı amaçlar. Bu araç, FTP sunucusuna bağlanarak farklı şifre kombinasyonlarını dener ve doğru şifreyi bulduğunda başarılı bir giriş yapar.

Bu aracın amacı, şifrelerinizi test etmek ve güvenlik açıklarını tespit etmektir. Lütfen bu aracı sadece **yetkilendirilmiş** sistemlerde ve etik hacking için kullanın.

## Özellikler

- FTP sunucusuna bağlantı kurarak kaba kuvvet yöntemi ile şifre denemesi yapar.
- Birden fazla şifreyi paralel olarak deneyebilir, böylece daha hızlı bir saldırı gerçekleştirir.
- Başarılı bir giriş durumunda, Discord sunucu ve hesap bilgilerini ekrana yazdırır.
- Kolayca kurulabilir ve kullanılabilir.
  
### Gerekli Kütüphanelerin Yüklenmesi

Öncelikle gerekli kütüphaneleri yüklemeniz gerekecek. `colorama` gibi ek kütüphaneleri yüklemek için terminal veya komut istemcisinde şu komutu çalıştırın:

```bash
pip install colorama
```

## Yükleme

Bu aracı çalıştırmak için aşağıdaki adımları takip edin:

1. GitHub deposundan bu projeyi bilgisayarınıza indirin:

```bash
git clone https://github.com/onemoriarty/FTP-BruteR.git
```

2. Proje klasörüne girin:

```bash
cd FTP-BruteR
```

3. Şimdi aracı kullanmaya başlayabilirsiniz.

## Çalıştırma

Aracı çalıştırmak için, `ftpbruter.py` dosyasını terminal veya komut istemcisinde aşağıdaki gibi çalıştırın:

```bash
python ftpbruter.py
```

Ardından, araç sizden FTP sunucu IP adresi, kullanıcı adı ve şifre listesi dosyasını isteyecek. Bu bilgileri girmeniz gerekecek.

**Örnek Çıktı:**

```
FTP saldırı uygulamasına hoş geldiniz!
----------------------------------------
Bu uygulama, FTP sunucusuna bağlanarak belirtilen şifrelerle giriş yapacaktır.
----------------------------------------

FTP sunucusunun IP adresini gir > 192.168.1.1
FTP sunucusunun kullanıcı adını gir : admin
FTP sunucusuna saldıracağın listeyi gir : passwords.txt
```

Ardından, araç belirtilen şifre listesindeki her şifreyi deneyecek ve başarılı bir giriş bulduğunda işlem tamamlanacaktır.

## Sonuçlar

Eğer doğru şifre bulunursa, ekrana şu tür bir çıktı yazdırılır:

```
Başarılı giriş bulundu! Kullanıcı: admin, Şifre: password123
Discord sunucusu: https://discord.gg/xyz
Discord : onemoriarty
```

Eğer doğru şifre bulunmazsa, şifre denemeleri sırasındaki her başarısız giriş:

```
Başarısız giriş: Kullanıcı: admin, Şifre: password456
```

şeklinde ekrana yazdırılır.

## İletişim

Eğer herhangi bir sorunuz veya öneriniz varsa, benimle iletişime geçebilirsiniz:
- **Discord nickim**: onemoriarty
- **Discord sunucumuz**: [warnight](https://discord.gg/QRppCpjvZc)
