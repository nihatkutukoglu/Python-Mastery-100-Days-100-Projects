# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 16:13:58 2025

@author: user
"""

#  ---------------- DAY 11 PROJECT : SAFE CALCULATOR -------------------------
def topla(x,y):
    return x + y 
def cikar(x,y):
    return x - y
def carp(x,y):
    return x*y
def bol(x,y):
    if y == 0:
        raise ZeroDivisionError("sıfıra bölemezsiniz.")
    return x / y 

def menu_goster():
    print("\n --- Güvenli Hesap Makinesine Hogeldiniz ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    
while True :
 menu_goster() 
 secim = input("1 - 5 arası seçim yapınız.")
 
 if secim == 5 :
     print("Yeniden görüşmek üzere...")
     break
 
 try :
    sayi1 = float(input("İlk sayıyı giriniz."))
    sayi2 = float(input("ikinci sayıyı giriniz."))
    
    if secim == "1":
      print("sonuc:" , topla(sayi1,sayi2))
      
    elif secim == "2" :
         print("sonuc:" , cikar(sayi1, sayi2))
    elif secim == "3" :
          print("sonuc:" , carp(sayi1, sayi2))    
    elif secim == "4":
        print("sonuc:" , bol(sayi1,sayi2))
    else:
        print("geçersiz seçim yaptınız.")

 except ValueError:
    print("Yanlış türde değer girdiniz")
 except ZeroDivisionError as e : #e hatayı direkt söyler. 
     print(f"hata : {e}")
 except Exception as e :
     print(f"beklenmeyen bir hata oluştu. Hata : {e}")
    
 finally:
    print("Güvenli Hesap Makinesini kullandığınız için teşekkürler!... Yeniden başlatılıyor...")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     

    
     
