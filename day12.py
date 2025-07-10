# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:21:46 2025

@author: user
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def menu_goster():
    print("\n--- Sıcaklık Dönüştürücü Menü ---")
    print("1. Celsius → Fahrenheit ve Kelvin")
    print("2. Fahrenheit → Celsius ve Kelvin")
    print("3. Kelvin → Celsius ve Fahrenheit")
    print("4. Çıkış")
    
while True:
    menu_goster()
    secim = input("Seçiminizi girin (1/2/3/4): ")

    if secim == '1':
        c = float(input("Celsius cinsinden sıcaklığı girin: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f} °F")
        print(f"Kelvin: {celsius_to_kelvin(c):.2f} K")

    elif secim == '2':
        f = float(input("Fahrenheit cinsinden sıcaklığı girin: "))
        print(f"Celsius: {fahrenheit_to_celsius(f):.2f} °C")
        print(f"Kelvin: {fahrenheit_to_kelvin(f):.2f} K")

    elif secim == '3':
        k = float(input("Kelvin cinsinden sıcaklığı girin: "))
        print(f"Celsius: {kelvin_to_celsius(k):.2f} °C")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.2f} °F")

    elif secim == '4':
        print("Programdan çıkılıyor. Hoşça kal!")
        break

    else:
        print("Geçersiz seçim. Lütfen (1/2/3/4) arası bir değer girin.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        