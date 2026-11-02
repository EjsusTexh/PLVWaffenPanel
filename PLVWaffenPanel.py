import time
import sys

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
while True:
    print("========================================")
    print("         PLUVWAFFEN PANEL V1.0          ")
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
        print("\n[!] Oturum kapatılıyor. Güvenli çıkış yapıldı.")
        break

    else:
        print("\n[!] Geçersiz bir seçim yaptınız! Lütfen 1-5 arasında bir değer girin.\n")
        time.sleep(1.5)