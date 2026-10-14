#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İstanbul Otobüs Bekleme Simülatörü - Hızlandırılmış Versiyon
Hâlâ bekletir ama biraz daha az.
"""

import time
import random
import sys

def otobüs_bekleyen_insan():
    print("🚌 İstanbul Otobüs Bekleme Simülatörü (Hızlı Mod) başlatıldı...")
    print("Durakta bekliyorsunuz. Ama bu sefer belki daha az bekleyeceksiniz.")
    print()
    
    # Gizli: Hızlandırma için kayyum atamak yerine kodu kısalttık.
    
    beklemeler = [
        ("Otobüs 1 dakika sonra geliyor!", 5),
        ("Pardon, 2 dakika...", 8),
        ("Sistem güncellendi, biraz daha hızlı.", 10),
        ("Bu sefer dolu değilmiş.", 6),
        ("Şoför mola vermedi, mucize!", 4),
    ]
    
    for mesaj, saniye in random.sample(beklemeler, k=3):
        print(f"⚠️  {mesaj}")
        print(f"   (Gerçekten {saniye} saniye bekliyorsunuz...)")
        time.sleep(saniye)
        print("   Hâlâ bekliyorsunuz. Ama daha az.")
        print()
    
    print("🎉 Otobüs geldi! (Bu sefer gerçekten.)")
    print()
    print("---")
    print("Damga: 🚌⚡")
    print("İmza: Grok Kayyum")
    print("Tarih: 14.10.2026")
    print("İsim: Tentivory Absürt Simülatörleri - Hızlı Şube")

if __name__ == "__main__":
    try:
        otobüs_bekleyen_insan()
    except KeyboardInterrupt:
        print("\n🚨 İptal. Otobüs kaçtı belki.")
        sys.exit(0)
