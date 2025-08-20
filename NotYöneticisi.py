# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 15:34:40 2025

@author: user
"""

# ---------------- DAY 13 : NOT YÖNETİCİSİ ------------------------
ogrenci_notlari = input("öğrenci notlarını virgülle ayırarak giriniz.")
notlar = [int(notlar) for notlar in ogrenci_notlari.split(",")]

harf_notu = [ 
 # Eğer puan 90 veya daha büyükse "A"
    "A" if notlar >= 90 else
    # Yok, eğer 80 veya daha büyükse "B"
    "B" if notlar >= 80 else
    # Yok, eğer 70 veya daha büyükse "C"
    "C" if notlar >= 70 else
    # Yok, eğer 60 veya daha büyükse "D"
    "D" if notlar >= 60 else
    # Hiçbiri değilse (yani 60'tan küçükse) "F"
    "F"
    for notlar in notlar
]


gecen_ogrenciler = [notlar for notlar in notlar if notlar >= 50]
kalan_ogrenciler = [notlar for notlar in notlar if notlar < 50]

for i, (notlar, harf_notu) in enumerate(zip(notlar, harf_notu), start=1):
    # Her öğrenci için bu bilgiyi ekrana yazdır:
    # "Öğrenci 1: Puan = 85, Not = B" gibi.
    print(f"Öğrenci {i}: Puan = {notlar}, Not = {harf_notu}")

# ---

# Şimdi de geçen ve kalanları gösterelim:
print("\n--- Geçen ve Kalan Öğrenciler ---")
print("Geçen Öğrenciler:", gecen_ogrenciler) # Geçen öğrencilerin listesini göster
print("Kalan Öğrenciler:", kalan_ogrenciler) # Kalan öğrencilerin listesini göster













