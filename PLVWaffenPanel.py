import time
import sys
import os

dongu_karakterleri = ["|", "/", "-", "\\"]

# --- BAŞLANGIÇ YÜKLEME EFEKTLERİ ---
print("--- EJSUS AUTISTIC TOOL V1.0 ---")
print("EjsusTexh sunucusuna bağlanılıyor", end="")
for i in range(3):
    time.sleep(1.8)
    print(".", end="", flush=True)
print(" [BAĞLANTI KURULDU]")
time.sleep(1.5)

for char in dongu_karakterleri:
    print(f"\r[*] Connecting to PluvWaffen Security System... {char}", end="", flush=True)
    time.sleep(3.0)
print("\r[*] Connecting to PluvWaffen Security System... [OK]")
time.sleep(0.6)
print("[✔] Admin-operation success!\n")

# --- ANA MENÜ DÖNGÜSÜ ---
import os
import time

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================")
    print("        PLUVWAFFEN PANEL V1.0           ")
    print("========================================")
    print("[1] Kullanıcı/Kayıt Deposu Sorgula")
    print("[2] Sistem Taraması Yap")
    print("[3] Sunucu Durumu Kontrol Et")
    print("[4] Ağ Trafiği İzle")
    print("[5] Çıkış Yap")
    print("========================================")

    secim = input("Lütfen bir işlem seçin (1-5): ")

    if secim == "1":
        isim = input("\nKullanıcı adı veya sicil no girin: ")
        
        if isim == "333":
            print("333 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Mustafa Burak Erdem")
            time.sleep(1.2)
            print("Köle")
            time.sleep(1.7)
            print("20 derece açı ile NUH soyundan.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "nuh":
            print("Nuh adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Faruk Çiloğlu")
            time.sleep(1.2)
            print("Faruk Files")
            time.sleep(1.7)
            print("The Great Creator of NUH.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "281":
            print("281 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Zekeriya Bilgin Açıkgöz")
            time.sleep(1.2)
            print("Paycell user")
            time.sleep(1.7)
            print("38 derecelik açı ile Nuh soyundan.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "osmand4l":
            print("osmand4l adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Osman Dal")
            time.sleep(1.2)
            print("Büyük Astro Fizikçi, OAL Halk ozanı , Galileoyu panelleyen adam")
            time.sleep(1.7)
            print("318 derece açı ile Nuh soyundan.\n")
            input("Devam etmek için Enter'a basın...")
	
        elif isim == "271":
            print("271 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Arif Esat Ateşmen")
            time.sleep(1.2)
            print("Paneli çok sever")
            time.sleep(1.7)
            print("43 derece açı ile Nuh soyundan.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "uchar":
            print("uchar adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Mustafa Uçar")
            time.sleep(1.2)
            print("Freddy Fazbear")
            time.sleep(1.7)
            print("NUH SOYUNUN BAŞ DÜŞMANI.\n")
            input("Devam etmek için Enter'a basın...")

        elif isim == "229":
            print("229 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Emre Gök")
            time.sleep(1.2)
            print("11/2/2026 tarihinde çok talihsiz bir olay yaşadı")
            time.sleep(1.7)
            print("21 derecelik açı ile Nuh soyundan.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "189":
            print("189 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("UNKNOWN.")
            time.sleep(1.2)
            print(".")
            time.sleep(1.7)
            print("CREATOR OF EJSUS_TEXH\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "41":
            print("41 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Mehmet Alper Yayar")
            time.sleep(1.2)
            print("roploks oynar")
            time.sleep(1.7)
            print("geçen hafta öldü o yüzden soy bilgisi yok.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "247":
            print("247 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("İbrahim Ekrem Çelik")
            time.sleep(1.2)
            print("RTX 5090, İburamin, League Of Legends")
            time.sleep(1.7)
            print("31 derece açı ile Nuh soyundan.\n")
            input("Devam etmek için Enter'a basın...")
            
        elif isim == "734":
            print("734 adlı kullanıcı deposu gösteriliyor:")
            time.sleep(2.0)
            print("Tunahan\n")
            input("Devam etmek için Enter'a basın...")
            
        else:
            print("Kullanıcı bulunamadı, NUH soyundan olup olmadığınızı kontrol edin. 10 saniye içinde menüye döneceksiniz.\n")
            time.sleep(10.0)

    elif secim == "2":
        print("\n[*] Sistem taranıyor...")
        time.sleep(1.5)
        print("[✔] Bütün sistemler stabilize durumda.\n")
        input("Devam etmek için Enter'a basın...")

    elif secim == "3":
        print("\n[*] Sunucu ping süreleri kontrol ediliyor...")
        time.sleep(1.5)
        print("[✔] Sunucu yanıt süresi: 12ms (Aktif)\n")
        input("Devam etmek için Enter'a basın...")

    elif secim == "4":
        print("\n[*] Ağ trafiği dinleniyor...")
        time.sleep(2.0)
        print("[✔] Şüpheli paket tespit edilmedi.\n")
        input("Devam etmek için Enter'a basın...")

    elif secim == "5":
        print("\n[✔] Oturum kapatılıyor. Güvenli çıkış yapıldı.")
        time.sleep(1.5)
        break

    else:
        print("\n[!] Geçersiz bir seçim yaptınız! Lütfen 1-5 arasında bir değer girin.\n")
        time.sleep(1.5)
