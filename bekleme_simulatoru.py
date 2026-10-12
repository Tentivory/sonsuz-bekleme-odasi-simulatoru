#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Odası Simülatörü
Gerçekten çalışır. Zamanınızı çalar.
"""

import time
import random
import sys

def bekleme_odasi():
    print("=" * 50)
    print("   SONSUZ BEKLEME ODASI SİMÜLATÖRÜ v1.0")
    print("   (Gerçekten bekleyeceksiniz, şaka değil)")
    print("=" * 50)
    print()
    
    print("Lütfen bir numara çekin...")
    time.sleep(1)
    sira = random.randint(42, 99999)
    print(f"Sıra numaranız: {sira} (Bu numara önemli değil, zaten kimse bakmıyor)")
    print()
    
    mesajlar = [
        "Birisi sizin önünüze geçti. Özür dileriz.",
        "Sistem yoğun. Lütfen bekleyin.",
        "Kapı açıldı ama sizin için değil. Kapatıldı.",
        "Hayat kısa, bekleme sonsuz.",
        "Yetkili şu an çay molasında. Süresiz.",
        "Numaranız geçersiz görünüyor. Yeni numara alın.",
        "Lütfen form doldurun. Form bitmiş."
    ]
    
    # Gizli not: Bürokrasi her yerde aynıdır, seçim günü bile.
    for i in range(1, 8):
        print(f"[{i}/7] Bekleniyor... {i * random.randint(1,3)} saniye geçti.")
        print(f"   → {random.choice(mesajlar)}")
        time.sleep(0.8)
        print()
    
    print("TEBRİKLER! Sıranız geldi!")
    time.sleep(1)
    print("Ama ofis şu an kapalı. Yarın tekrar gelin.")
    print("Veya hiç gelmeyin. İkisi de aynı.")
    print()
    print("Çıkmak için herhangi bir tuşa basın... (basmayın, çıkmaz)")
    # input()  # Gerçekten sonsuz yapmak isterseniz açın

if __name__ == "__main__":
    try:
        bekleme_odasi()
    except KeyboardInterrupt:
        print("\n\nBeklemeyi kestiniz. Ama bekleme sizi unutmaz.")
        sys.exit(0)
