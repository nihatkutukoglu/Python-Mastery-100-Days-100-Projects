# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 19:33:38 2025

@author: user
"""

# ------- DAY 16 PROJECT : GÜNLÜK PROGRAMI ------- 

def gunkayit_ekle():
    gunkayit = input("Günlük kaydınızı giriniz")
    with open ("günlük.txt","a") as file :
        file.write(gunkayit + "\n")
    print(" günlük kaydınız başarıyla eklenmiştir. ")
    
def kayitlari_goster() :
    try:
        with open ("günlük.txt","r") as file :
            content = file.read()
            if content :
                print(content)
                print("günlük kaydınız başarıyla görüntülenmiştir.")
            else :
                print("günlük kaydı bulunamadı.")
    except FileNotFoundError() :
        print("dosya bulunamadı")
        
def gunlukkayit_bul() :
    anahtar_kelime = input("Arama yapmak için anahtar kelimeyi giriniz : ").lower()
    try:
        with open ("günlük.txt","r") as file:
            content = file.readlines()
            found = False
            print("--- arama sonuçları : --- ")
            for gunkayit in content :
                if anahtar_kelime in gunkayit.lower() :
                    print(gunkayit.strip())
                    found = True
                if not found : 
                    print("kayıt bulunmadı.")
    except FileNotFoundError:
        print("kayt bulunmadı")
                    
def menu_goster() :
    print("\n--- Günlük Menüsü ---")
    print("1. Yeni bir girdi ekle")
    print("2. Tüm girdileri görüntüle")
    print("3. Anahtar kelimeye göre girdileri ara")
    print("4. Çıkış")
                    
                    
while True :
    menu_goster()
    choice = input("seçim yapınız (1-4)")
    
    if choice == "1" :
        gunkayit_ekle()
        
    elif choice == "2" :
        kayitlari_goster()
    
    elif choice == "3" :
        gunlukkayit_bul()
        
    elif choice == "4" :
        print("Çıkış yapılıyor..")
        break
    

    else :
        print("Yanlış seçim yapıldı.")


  





















           
                    
                    
                    
                    
                    
                    
                    
                    
                    
