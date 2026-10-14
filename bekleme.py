#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İstanbul Otobüs Bekleme Simülatörü
Gerçekten bekletir. Gerçekten.
"""

import time
import random
import sys

def otobüs_bekleyen_insan():
    print("🚌 İstanbul Otobüs Bekleme Simülatörü başlatıldı...")
    print("Durakta bekliyorsunuz. Hava soğuk, moral düşük.")
    print("Otobüs ne zaman gelecek? Kimse bilmiyor. Biz de bilmiyoruz.")
    print()
    
    # Gizli siyasi referans (yorum satırında saklı)
    # Bazı şehirlerde otobüsler kayyum sayesinde daha düzenli çalışıyor derler. Doğru mu? Bu simülatör cevap vermez.
    
    beklemeler = [
        ("Otobüs 2 dakika sonra geliyor!", 15),
        ("Pardon, 5 dakika...", 30),
        ("Sistem güncelleniyor, biraz bekleyin.", 45),
        ("Bir önceki otobüs doluydu, bu da dolu olacak.", 20),
        ("Şoför mola verdi, anlaşırız.", 60),
        ("Trafik var, normal.", 25),
        ("Bir sonraki durakta inecekmiş gibi yapanlar yüzünden gecikiyor.", 10),
        ("Otobüs geldi! ... Şaka yaptım.", 40),
    ]
    
    for mesaj, saniye in random.sample(beklemeler, k=5):
        print(f"⚠️  {mesaj}")
        print(f"   (Gerçekten {saniye} saniye bekliyorsunuz...)")
        time.sleep(saniye)  # Gerçek bekleme!
        print("   Hâlâ bekliyorsunuz. Tebrikler.")
        print()
    
    print("🎉 Otobüs nihayet geldi! Ya da gelmedi. Program bitti.")
    print("Bir sonraki seferde daha şanslı olursunuz. Belki.")
    print()
    print("---")
    print("Damga: 🚌")
    print("İmza: Grok Kayyum")
    print("Tarih: 14.10.2026")
    print("İsim: Tentivory Absürt Simülatörleri")

if __name__ == "__main__":
    try:
        otobüs_bekleyen_insan()
    except KeyboardInterrupt:
        print("\n🚨 Simülasyon iptal edildi. Gerçek hayatta otobüs de gelmeyebilir.")
        sys.exit(0)
