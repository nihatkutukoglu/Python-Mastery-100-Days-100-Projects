# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 13:45:33 2025

@author: user
"""

#  --------------------- DAY 10 NOTE PROJECT ----------------------------------
# Step 1 : Dosya oluştur. 
with open ("MyNotes.txt","r") as file :
    icerik=file.read() 
    
# Step 2: Menü göster.
def show_menu() :
    print("\n --- Not Alma Uygulaması ---")
    print("1. Not ekle")
    print("2. Tüm notları görüntüle")
    print("3. Tüm notları sil")
    print("4. Çıkış")
    
# Step 3: Yeni not ekleme :
def add_note():
    note = input("Notunuzu giriniz:")
    with open ("MyNotes.txt","a") as file :
     file.write(note + "\n" )
     print("notunuz başarılı bir şekilde eklendi.")
     
# Step 4: Bütün notları görüntüleme :

def view_notes():
    try:
        with open("MyNotes.txt", "r") as file:
            content = file.read()
            if content:
                print("\n--- Notların ---")
                print(content)
            else:
                print("\n Not bulunamadı")
    except FileNotFoundError:
        print("not bulunamadı.")

# step 5 tüm notları sil

def notlari_sil():
   onay = input("Bütün notları silmek istediğinize emin misiniz? (evet/hayır")
   if onay == "yes":
       with open ("MyNotes.txt","w") as file :
           file.write("")
       print("tüm notlar silindi")
   else:
       print("silme işlemi iptal edildi.")
    
# step 6  : Ana program döngüsü 

while True : 
    show_menu()
    choice = input("seçeneceği seçin (1-4)")
    if choice == "1" :
        add_note()
    elif choice == "2" :
        view_notes()
    elif choice == "3" :
        notlari_sil()
    elif choice == "4" :
        print("Not alma uygulamasından çıkış yapılıyor. ")
        break 
    else: 
        print("geçersiz seçim. Lütfen tekrardan deneyiniz.")














































    